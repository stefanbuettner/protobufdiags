#!/usr/bin/env python
"""
Asdf
"""
from argparse import ArgumentParser
from google.protobuf import text_format
import caffe
from caffe.proto import caffe_pb2

def parse_args():
    """Parse input arguments
    """

    parser = ArgumentParser(description="Output some meta info for the given neural network.")

    parser.add_argument('input_net_proto_file',
                        help='Input network prototxt file')
    #parser.add_argument('--rankdir',
    #                    help=('One of TB (top-bottom, i.e., vertical), '
    #                          'RL (right-left, i.e., horizontal), or another '
    #                          'valid dot option; see '
    #                          'http://www.graphviz.org/doc/info/'
    #                          'attrs.html#k:rankdir'),
    #                    default='LR')
    parser.add_argument('--phase',
                        help=('Which network phase to draw: can be TRAIN, '
                              'TEST, or ALL.  If ALL, then all layers are drawn '
                              'regardless of phase.'),
                        default="ALL")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    net = caffe_pb2.NetParameter()
    text_format.Merge(open(args.input_net_proto_file).read(), net)
    phase=None;
    if args.phase == "TRAIN":
        phase = caffe.TRAIN
    elif args.phase == "TEST":
        phase = caffe.TEST
    elif args.phase != "ALL":
        raise ValueError("Unknown phase: " + args.phase)
    print(net.name)
#    caffe.draw.draw_net_to_file(net, args.output_image_file, args.rankdir,
#                                phase)

if __name__ == '__main__':
    main()

