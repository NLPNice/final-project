from glob import glob
import pandas as pd
from lxml import etree, html


def parse_desc(xml):
    description = html.fromstring(xml)

    sections = dict()
    headings = [e.tag == "heading" for e in description]
    if True in headings:
        description = description[headings.index(True):]
        # group all paragraphs from the same section
        i = 0
        section_i = 0
        cur_section = None
        while i < len(description):
            if description[i].tag == "heading":
                cur_section = description[i].text_content()
                sections[cur_section] = list()
            elif description[i].tag is not etree.Comment:
                sections[cur_section].append(description[i].text_content())
            i += 1
    else:
        sections['Heandingless description'] = description.text_content()

    return sections

def parse_claim(xml):
    tree = html.fromstring(xml)
    claims = tree.xpath("//claim")
    claims = [''.join(c.text_content()) for c in claims]
    return claims

files = glob('*.txt')

out_claim_df = None
out_descr_df = None
out_title_df = None

for f in files:
    print('processing file ', f)
    data = pd.read_csv(f, sep='\t', header=None, names = ["PatenType", "PatentNumber", "PublicationType", "Date", "Language", "Part", "Number", "Contents"])
    data = data.loc[data["Language"] == "en"]
    data = data.loc[data["PublicationType"] == "B1"]
    data = data.loc[data["Part"] != "PDFEP"]
    data = data.reset_index(drop=True)

    df_Descr = data[data["Part"] == "DESCR"].reset_index(drop=True)
    descr_patents = df_Descr['PatentNumber'].unique()
    descr_df = data[data['PatentNumber'].isin(descr_patents)]
    df_Titles = descr_df[descr_df["Part"] == "TITLE"].reset_index(drop=True)
    df_Claim = descr_df[descr_df["Part"] == "CLAIM"].reset_index(drop=True)

    df_Descr["Contents"] = df_Descr["Contents"].apply(parse_desc)
    df_Claim["Contents"] = df_Claim["Contents"].apply(parse_claim)

    if out_claim_df is None:
        out_claim_df = df_Claim
        out_descr_df = df_Descr
        out_title_df = df_Titles
    else:
        out_claim_df.append(df_Claim)
        out_descr_df.append(df_Descr)
        out_title_df.append(df_Titles)

out_descr_df.to_csv("out_descr.csv")
out_claim_df.to_csv("out_claim.csv")
out_title_df.to_csv("out_title.csv")