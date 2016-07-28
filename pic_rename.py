import os
import sys
import shutil
import datetime
from PIL import Image
from sys import argv
import PIL.ExifTags


def get_exif_data(file_name, input_directory):
    image_location = '{0}/{1}'.format(input_directory, file_name)
    img = Image.open(image_location)
    # Dictionary of EXIF numeric tags.
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    parsed_exif_data = {
        'image_instance' : img,
        'image_name' : file_name,
        'date' : 'NA',
        'lens_make' : 'NA',
        'lens_model' : 'NA'
    }
    if 'DateTimeDigitized' in exif.keys():
        parsed_exif_data['date'] = format_date(exif['DateTimeDigitized'])
    if 'LensMake' in exif.keys():
        parsed_exif_data['lens_make'] = exif['LensMake']
    if 'LensModel' in exif.keys():
        parsed_exif_data['lens_model'] = exif['LensModel']

    return parsed_exif_data

def format_date(date_string):
    return datetime.datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')

def rename_pics(input_directory, output_directory):
    if (os.path.exists(input_directory)):
        # Check output directory
        if not (os.path.exists(output_directory)):
            print "The Output Directory {0} was not found, but has been created".format(output_directory)
            os.makedirs(output_directory)
        files = os.listdir(input_directory)
        non_image_files = []
        image_files = []
        # get only the image files
        for f in files:
            if f.endswith('.JPG'):
                image_data = get_exif_data(f, input_directory)
                image_files.append(image_data)
            else:
                non_image_files.append(f)
        # Sort Images by the Date Taken
        image_files = sorted(image_files, key=lambda k: k['date'])
        for i in xrange(len(image_files)):
            num = i + 1
            digits = len(str(num))
            new_file_name = '{0}_{1}_{2}'.format(num, image_files[i]['date'], image_files[i]['lens_make'])
            new_file_full_path = '{0}/{1}'.format(output_directory, new_file_name)
            print 'Currently saving to {0}'.format(new_file_full_path)
            img = image_files[i]['image_instance']
            img.save(new_file_full_path, "JPEG")



if __name__ == '__main__':
    # Unpack script parameters
    script, input_directory, output_directory = argv
    rename_pics(input_directory, output_directory)
    # if (os.path.exists(input_directory)):
    #     # Check output directory
    #     if not (os.path.exists(output_directory)):
    #         print "The Output Directory {0} was not found, but has been created".format(output_directory)
    #         os.makedirs(output_directory)
    #     files = os.listdir(input_directory)
    #     non_image_files = []
    #     image_files = []
    #     # get only the image files
    #     for f in files:
    #         if f.endswith('.JPG'):
    #             image_data = get_exif_data(f, input_directory)
    #             image_files.append(image_data)
    #         else:
    #             non_image_files.append(f)
    #     # Sort Images by the Date Taken
    #     image_files = sorted(image_files, key=lambda k: k['date'])
    #     for i in xrange(len(image_files)):
    #         num = i + 1
    #         digits = len(str(num))
    #         new_file_name = '{0}_{1}_{2}'.format(num, image_files[i]['date'], image_files[i]['lens_make'])
    #         new_file_full_path = '{0}/{1}'.format(output_directory, new_file_name)
    #         print 'Currently saving to {0}'.format(new_file_full_path)
    #         img = image_files[i]['image_instance']
    #         # img.save(new_file_full_path, "JPEG")
