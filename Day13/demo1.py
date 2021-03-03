import xml.etree.ElementTree as ET


def create_xml():
    ## create node
    root = ET.Element('InterventionEvent')  # Root element
    input_ = ET.SubElement(root, 'Input') # Adding Input element
    input_child_sitename = ET.SubElement(input_, 'SiteName') 
    input_child_app = ET.SubElement(input_, 'Application') 
    input_child_type = ET.SubElement(input_, 'EventType') 
    input_child_descrip = ET.SubElement(input_, 'EventDescription') 
    input_child_comment = ET.SubElement(input_, 'EventComment') 
    input_child_equip = ET.SubElement(input_, 'EventData') 
    input_child_equip.set('Label', 'Equipment')
    input_child_time = ET.SubElement(input_, 'EventData') 
    input_child_time.set('Label', 'ProcessEndDateTime')
    lot = ET.SubElement(input_, 'Lot') 
    lot_child = ET.SubElement(lot, 'LotId') 
    lot_stepname = ET.SubElement(lot, 'StepName') 
    ## input text inside the node.
    input_child_sitename.text = 'HIROSHIMA'
    input_child_app.text = 'PHOTO_DATA'
    input_child_type.text = 'PHOTO_DATA'
    input_child_descrip.text = 'Nikon Exposure Log BDIS'
    input_child_comment.text = 'Nikon Exposure Log BDI'
    input_child_equip.text = 'ToolName'
    input_child_time.text = '2021/03/03'
    lot_child.text = 'LotID'
    lot_stepname.text = 'MFG_PROCESS_STEP'
    ## create the wafer list in dataframes
    for row in range(10):
        ## create each wafer node, waferscribe, waferId. slotNo
        wafer = ET.SubElement(lot, 'Wafer')
        wafer_scribe = ET.SubElement(wafer, 'WaferScribe')
        wafer_id = ET.SubElement(wafer, 'WaferID')
        wafer_slotNo = ET.SubElement(wafer, 'SlotNo')
        ## input text inside the wafer node.
        wafer_scribe.text = 'wafer_scribe_{}'.format(row)
        wafer_id.text = 'WAFER_ID_{}'.format(row)
        wafer_slotNo.text = str(row)

        ## create each wafer's measurement node.
        measurement = ET.SubElement(wafer, 'Measurement')
        measurement_type = ET.SubElement(measurement, 'Type')
        measurement_recipe = ET.SubElement(measurement, 'Recipe')
        measurement_tool = ET.SubElement(measurement, 'MetricTool')
        measurement_time = ET.SubElement(measurement, 'TimeStamp')
        ## Max_X
        measurement_max_X = ET.SubElement(measurement, 'Point')
        measurement_max_X.set('Label', 'LVLMEAN_MAX_X')
        measurement_max_X.set('Index', '1')
        ## Max_Y
        measurement_max_Y = ET.SubElement(measurement, 'Point')
        measurement_max_Y.set('Label', 'LVLMEAN_MAX_Y')
        measurement_max_Y.set('Index', '2')
        ## Min_X
        measurement_min_X = ET.SubElement(measurement, 'Point')
        measurement_min_X.set('Label', 'LVLMEAN_MIN_X')
        measurement_min_X.set('Index', '3')
        ## Min_Y
        measurement_min_Y = ET.SubElement(measurement, 'Point')
        measurement_min_Y.set('Label', 'LVLMEAN_MIN_Y')
        measurement_min_Y.set('Index', '4')
        ## AF_MAX
        measurement_af_max = ET.SubElement(measurement, 'Point')
        measurement_af_max.set('Label', 'AFMEAN_MAX')
        measurement_af_max.set('Index', '5')
        ## AF_MIN
        measurement_af_min = ET.SubElement(measurement, 'Point')
        measurement_af_min.set('Label', 'AFMEAN_MIN')
        measurement_af_min.set('Index', '6')
        ## input text inside the measurement node.
        measurement_type.text = 'WAFERDATA'
        measurement_recipe.text = 'Exposure Log'
        measurement_tool.text = 'ToolName'
        measurement_time.text = '2021/03/03'
        measurement_max_X.text = 'LvlMeanMaxX_{}'.format(row)
        measurement_max_Y.text = 'LvlMeanMaxY_{}'.format(row)
        measurement_min_X.text = 'LvlMeanMinX_{}'.format(row)
        measurement_min_Y.text = 'LvlMeanMinY_{}'.format(row)
        measurement_af_max.text = 'AFMeanMax_{}'.format(row)
        measurement_af_min.text = 'AFMeanMin_{}'.format(row)

    return ET.tostring(root)  # binary string


def save_xml_file(xml_data):
    with open("test.xml", 'w') as f:  # Write in file as utf-8
        f.write(xml_data.decode('utf-8'))


def main():
    xml_data = create_xml()
    save_xml_file(xml_data)


if __name__ == '__main__':
    main()