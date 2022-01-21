

import camelot as cm

def extract_table_into_csv(fname, pageno, savedirectory):
    tables = cm.read_pdf(fname, pages = pageno, flavor = 'stream')
    tables

    tables[0]

    # print (tables[1].parsing_report)

    # print (tables[1].df)

    tables[1].to_csv(savedirectory)
    return()

# tables[0].to_csv('foo.csv')
extract_table_into_csv((r"C:\Users\home\Documents\Python-Programs\keppel.pdf"), "69", (r"C:\Users\home\Documents\Python-Programs\keppel.csv"))
