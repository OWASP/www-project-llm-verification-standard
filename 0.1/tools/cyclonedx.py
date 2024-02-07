#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' CycloneDX converter class

    Converts the ASVS JSON into CycloneDX Standards format
    Copyright (c) 2023 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import json
from dicttoxml2 import dicttoxml
import datetime
import uuid
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CycloneDX:
    bom = {}
    bom['bomFormat'] = "CycloneDX"
    bom['specVersion'] = "1.6"
    bom['serialNumber'] = "urn:uuid:" + str(uuid.uuid4())
    bom['version'] = 1
    bom['metadata'] = {}
    bom['metadata']['timestamp'] = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    bom['metadata']['licenses'] = []
    bom['metadata']['licenses'].append({})
    bom['metadata']['licenses'][0]['license'] = {}
    bom['metadata']['licenses'][0]['license']['id'] = "CC-BY-SA-4.0"
    bom['metadata']['licenses'][0]['license']['url'] = "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt"
    bom['metadata']['supplier'] = {}
    bom['metadata']['supplier']['name'] = "OWASP Foundation"
    bom['metadata']['supplier']['url'] = [ "https://owasp.org" ]
    bom['declarations'] = {}
    bom['declarations']['standards'] = []
    bom['declarations']['standards'].append({})

    def __init__(self, llmsvs_json_in):
        self.llmsvs = llmsvs_json_in
        llmsvs = json.loads(llmsvs_json_in)
        bom_ref = llmsvs["ShortName"] + "-" + llmsvs["Version"]
        self.bom['declarations']['standards'][0]['bom-ref'] = bom_ref
        self.bom['declarations']['standards'][0]['name'] = \
            llmsvs["Name"].replace('Project', '') + "(" + llmsvs["ShortName"] + ")"
        self.bom['declarations']['standards'][0]['version'] = llmsvs["Version"]
        self.bom['declarations']['standards'][0]['description'] = llmsvs["Description"]
        self.bom['declarations']['standards'][0]['owner'] = llmsvs["Name"]

        requirements = []
        l1_requirements = []
        l2_requirements = []
        l3_requirements = []
        for llmsvs_chapter in llmsvs['Requirements']:
            chapter_req = self.convert_requirement(llmsvs_chapter, None)
            requirements.append(chapter_req)
            if 'Items' in llmsvs_chapter:
                for llmsvs_section in llmsvs_chapter['Items']:
                    section_req = self.convert_requirement(llmsvs_section, chapter_req['bom-ref'])
                    requirements.append(section_req)
                    for llmsvs_requirement in llmsvs_section['Items']:
                        requirement = self.convert_requirement(llmsvs_requirement, section_req['bom-ref'])
                        requirements.append(requirement)
                        if 'L1' in llmsvs_requirement and 'Required' in llmsvs_requirement['L1'] and llmsvs_requirement['L1']['Required'] is True:
                            l1_requirements.append(requirement['bom-ref'])
                        if 'L2' in llmsvs_requirement and 'Required' in llmsvs_requirement['L2'] and llmsvs_requirement['L2']['Required'] is True:
                            l2_requirements.append(requirement['bom-ref'])
                        if 'L3' in llmsvs_requirement and 'Required' in llmsvs_requirement['L3'] and llmsvs_requirement['L3']['Required'] is True:
                            l3_requirements.append(requirement['bom-ref'])

        self.bom['declarations']['standards'][0]['requirements'] = requirements

        self.bom['declarations']['standards'][0]['levels'] = []
        self.bom['declarations']['standards'][0]['levels'].append({})
        self.bom['declarations']['standards'][0]['levels'][0] = {}
        self.bom['declarations']['standards'][0]['levels'][0]['bom-ref'] = "level-1"
        self.bom['declarations']['standards'][0]['levels'][0]['identifier'] = "Level 1"
        self.bom['declarations']['standards'][0]['levels'][0]['description'] = "llmsvs Level 1 is for low assurance levels, and is completely penetration testable."
        self.bom['declarations']['standards'][0]['levels'][0]['requirements'] = l1_requirements
        self.bom['declarations']['standards'][0]['levels'].append({})
        self.bom['declarations']['standards'][0]['levels'][1] = {}
        self.bom['declarations']['standards'][0]['levels'][1]['bom-ref'] = "level-2"
        self.bom['declarations']['standards'][0]['levels'][1]['identifier'] = "Level 2"
        self.bom['declarations']['standards'][0]['levels'][1]['description'] = "llmsvs Level 2 is for applications that contain sensitive data, which requires protection and is the recommended level for most apps."
        self.bom['declarations']['standards'][0]['levels'][1]['requirements'] = l2_requirements
        self.bom['declarations']['standards'][0]['levels'].append({})
        self.bom['declarations']['standards'][0]['levels'][2] = {}
        self.bom['declarations']['standards'][0]['levels'][2]['bom-ref'] = "level-3"
        self.bom['declarations']['standards'][0]['levels'][2]['identifier'] = "Level 3"
        self.bom['declarations']['standards'][0]['levels'][2]['description'] = "llmsvs Level 3 is for the most critical applications - applications that perform high value transactions, contain sensitive medical data, or any application that requires the highest level of trust."
        self.bom['declarations']['standards'][0]['levels'][2]['requirements'] = l3_requirements

        self.bom['declarations']['standards'][0]['externalReferences'] = []
        self.bom['declarations']['standards'][0]['externalReferences'].append({})
        self.bom['declarations']['standards'][0]['externalReferences'][0]['type'] = 'website'
        self.bom['declarations']['standards'][0]['externalReferences'][0]['url'] = 'https://owasp.org/llmsvs'
        self.bom['declarations']['standards'][0]['externalReferences'].append({})
        self.bom['declarations']['standards'][0]['externalReferences'][1]['type'] = 'vcs'
        self.bom['declarations']['standards'][0]['externalReferences'][1]['url'] = 'https://github.com/OWASP/llmsvs'
        self.bom['declarations']['standards'][0]['externalReferences'].append({})
        self.bom['declarations']['standards'][0]['externalReferences'][2]['type'] = 'issue-tracker'
        self.bom['declarations']['standards'][0]['externalReferences'][2]['url'] = 'https://github.com/OWASP/llmsvs/issues'
        self.bom['declarations']['standards'][0]['externalReferences'].append({})
        self.bom['declarations']['standards'][0]['externalReferences'][3]['type'] = 'social'
        self.bom['declarations']['standards'][0]['externalReferences'][3]['url'] = 'https://twitter.com/OWASP_llmsvs'

    def convert_requirement(self, llmsvs_requirement, parent):
        requirement = {}
        requirement['bom-ref'] = llmsvs_requirement['Shortcode']
        requirement['identifier'] = llmsvs_requirement['Shortcode']
        if 'ShortName' in llmsvs_requirement and llmsvs_requirement['ShortName'] != '':
            requirement['title'] = llmsvs_requirement['ShortName']
        if 'Name' in llmsvs_requirement and llmsvs_requirement['Name'] != '':
            requirement['title'] = llmsvs_requirement['Name']
        if 'Description' in llmsvs_requirement and llmsvs_requirement['Description'] != '':
            requirement['text'] = llmsvs_requirement['Description']
        if parent:
            requirement['parent'] = parent
        return requirement

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.bom, indent = 2, sort_keys = False, ensure_ascii=False).strip()
