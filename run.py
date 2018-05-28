#!/usr/bin/env python
import argparse
from style_transfer import style_transfer
from adain.util import get_params

if __name__ == '__main__':
    params = get_params(style_transfer)
    parser = argparse.ArgumentParser(description='AdaIN Style Transfer')

    parser.add_argument('--content', help='File path to the content image')
    parser.add_argument('--content_dir', help="""Directory path to a batch of
        content images""")
    parser.add_argument('--style', help="""File path to the style image,
        or multiple style images separated by commas if you want to do style
        interpolation or spatial control""")
    parser.add_argument('--style_dir', help="""Directory path to a batch of
        style images""")
    parser.add_argument('--vgg_weights', default=params['vgg_weights'],
        help='Path to the weights of the VGG19 network')
    parser.add_argument('--decoder_weights', default=params['decoder_weights'],
        help='Path to the decoder')

    parser.add_argument('--content_size', default=params['content_size'],
        type=int, help="""Maximum size for the content image, keeping
        the original size if set to 0""")
    parser.add_argument('--style_size', default=params['style_size'], type=int,
        help="""Maximum size for the style image, keeping the original
        size if set to 0""")
    parser.add_argument('--crop_style', action='store_true', help="""If set, center
        crop style image before processing""")
    parser.add_argument('--crop', action='store_true', help="""If set, center
        crop content image before processing""")
    parser.add_argument('--save_ext', default=params['save_ext'],
        help='The extension name of the output image')
    parser.add_argument('--gpu', default=params['gpu'], type=int,
        help='Zero-indexed ID of the GPU to use; for CPU mode set to -1')
    parser.add_argument('--output_dir', default=params['output_dir'],
        help='Directory to save the output image(s)')

    parser.add_argument('--preserve_color', action='store_true',
        help='If set, preserve color of the content image')
    parser.add_argument('--alpha', default=params['alpha'], type=float,
        help="""The weight that controls the degree of stylization. Should be
        between 0 and 1""")
    parser.add_argument('--style_interp_weights', help="""The weight for
        blending the style of multiple style images""")
    parser.add_argument('--mask', help="""Mask to apply spatial
        control, assume to be the path to a binary mask of the same size as
        content image""")

    args = parser.parse_args()
    output_images = style_transfer(**vars(args))
    print(output_images)
