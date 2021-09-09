# Your imports go here
import logging
import os
import json
import re
logger = logging.getLogger(__name__)
'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    ocr_file = os.path.join(dirpath, 'ocr.json')
    text = []
    with open(ocr_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in range(len(data["Blocks"])):
            if 'Text' in data["Blocks"][i]:
                obj = re.sub('[A-Za-z,]', '', data["Blocks"][i]["Text"])
                obj = obj.replace('$', '')
                if re.match(r'\d+\.\d+', obj):
                    text.append(float(obj))
    return max(text)
