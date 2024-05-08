# %%
!pip3 install -U sec-edgar-downloader
!pip3 install -q -U google-generativeai
!pip3 install -q -U google-generativeai --upgrade
!pip3 install python-dotenv
!pip3 install fpdf
!pip3 install pip --upgrade
!pip3 install pyopenssl --upgrade

# %%
from sec_edgar_downloader import Downloader

# Download filings to the current working directory
dl = Downloader("Georgia Tech", "dsharma97@gatech.edu", ".")

# %%
# Get the latest supported filings, if available, for a
# specified list of tickers and CIKs
equity_ids = ["AAPL", "MSFT", "GOOG"]
for equity_id in equity_ids:
    dl.get("10-K", equity_id, after='1994-12-31', before='2024-01-01')

# %%
# import os
# import textwrap
# from fpdf import FPDF

# def text_to_pdf(text, filename):
#     a4_width_mm = 210
#     pt_to_mm = 0.35
#     fontsize_pt = 10
#     fontsize_mm = fontsize_pt * pt_to_mm
#     margin_bottom_mm = 10
#     character_width_mm = 7 * pt_to_mm
#     width_text = a4_width_mm / character_width_mm

#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#     pdf.set_auto_page_break(True, margin=margin_bottom_mm)
#     pdf.add_page()
#     pdf.set_font(family='Courier', size=fontsize_pt)
#     splitted = text.split('\n')

#     for line in splitted:
#         lines = textwrap.wrap(line, width_text)

#         if len(lines) == 0:
#             pdf.ln()

#         for wrap in lines:
#             pdf.cell(0, fontsize_mm, wrap, ln=1)

#     pdf.output(filename, 'F')


# for company_ticker in os.listdir("./sec-edgar-filings"):
#     directory = "./sec-edgar-filings/{}/10-K".format(company_ticker)
#     for folder in os.listdir(directory):
#         folder_path = os.path.join(directory, folder)
#         filename = os.listdir(folder_path)[0]
#         file_path = os.path.join(folder_path, filename)
#         if filename.endswith('.txt'):
#             print(filename)
#             pdf_file = file_path[:-4]+".pdf"
#             file = open(file_path)
#             text = file.read()
#             file.close()
#             text_to_pdf(text, pdf_file)

# %%
import pathlib
import textwrap
import google.generativeai as genai
import os

from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")


# %%
%%time
response = model.generate_content("What is the meaning of life?")
print(response)

# %%
to_markdown(response.text)

# %%
import os
import re

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

company_ticker = 'AAPL'

directory = "./sec-edgar-filings/{}/10-K".format(company_ticker)

parts = ["Using the following 29 years worth of SEC-Edgar 10-K fillings for the company {}, give me specific analytics and insights about the company: financial analysis (to track metrics like revenue over time), sentiment analysis, and specific observations.".format(company_ticker)]


for folder in os.listdir(directory):
    folder_path = directory+"/"+folder
    filename = os.listdir(folder_path)[0]
    print(filename)
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            year = file.readline()[-9:]
        text = "SEC Filling for Year {} - Inputted in HTML formatting:\n".format(year)
        print(folder)
        with open(file_path) as myfile:
            content = myfile.read()
        filetxt = read_text_from_file(file_path)

        analyze = re.search(r'Company Stock Performance.*?Operating Expenses', content, re.DOTALL)
        if not analyze:
            analyze = re.search(r'Company Stock Performance.{20000}', content, re.DOTALL)
        if not analyze:
            analyze = re.search(r"Item *5.{20000}", content, re.DOTALL)

        analyze = analyze.group()[:20000]
        print(analyze)
        text += analyze
        #text += read_text_from_file(file_path)
        #upload_filename = "{}-{}:".format(company_ticker, year)
        #print(upload_filename)
        #f = genai.upload_file(file_path, display_name=upload_filename)
        #print(f)
        parts.append(text)

# %%
messages = [
    {'role':'user',
     'parts': parts}
]
print(parts)
response = model.generate_content(messages, request_options={"timeout": 600})
to_markdown(response.text)

# %% [markdown]
# > ## Apple Inc. (AAPL): Analysis of SEC Filings from 1995 to 2023
# > 
# > Based on the provided excerpts from AAPL's 10-K filings, here's an overview of the company's performance and sentiment over time:
# > 
# > **Financial Analysis:**
# > 
# > * **Revenue:** Apple experienced significant growth in the late 1990s and early 2000s, driven by the success of the iMac and later, the iPod. The introduction of the iPhone in 2007 marked another turning point, propelling the company to even greater heights. In recent years, revenue growth has stabilized but remains substantial, with Services becoming an increasingly important revenue stream.
# > * **Net Income:** Similar to revenue, net income followed a similar trajectory, demonstrating profitability alongside growth. However, there were periods of losses in the late 1990s due to restructuring and challenges in the personal computer market.
# > * **Earnings Per Share (EPS):** EPS trends closely mirror net income, reflecting the company's profitability on a per-share basis. 
# > * **Cash and Investments:** Apple's cash and short-term investments have steadily increased over the years, indicating strong financial health and the ability to invest in future growth opportunities.
# > * **Total Assets and Liabilities:** Both total assets and liabilities have grown substantially, reflecting the expansion of the company's operations and financial activities. 
# > 
# > **Sentiment Analysis:**
# > 
# > * **Early Years (1995-2000):** Filings from this period express concerns about the highly competitive personal computer market, pricing pressures, and challenges related to product transitions. There was a focus on managing costs and improving efficiency. 
# > * **Growth Era (2001-2013):** Sentiment becomes more positive as Apple experiences tremendous success with the iPod, iPhone, and iPad. The company emphasizes its innovation, design, and integrated digital lifestyle solutions. 
# > * **Mature Phase (2014-2023):** Filings acknowledge the mature nature of some of its core markets but remain optimistic about future growth prospects. The company highlights the importance of Services and its expanding ecosystem.
# > 
# > **Specific Observations:**
# > 
# > * **Shift in Product Mix:** The filings show a clear shift in Apple's product mix over time, from primarily focusing on Macintosh computers to a more diversified portfolio encompassing iPhones, iPads, wearables, and services.
# > * **International Expansion:** Apple has consistently emphasized the importance of international markets, with international sales constituting a significant portion of its total revenue.
# > * **Competitive Landscape:** The company acknowledges the intense competition it faces in various markets, particularly from other technology giants and emerging players. 
# > * **Focus on Innovation:** Innovation remains a core theme throughout the filings, with Apple consistently highlighting its commitment to research and development and bringing new products and technologies to market.
# > 
# > **Limitations:**
# > 
# > * **This analysis is based on excerpts and summaries of the 10-K filings and may not capture the full complexity of the company's financial performance and sentiment.**
# > * **The filings only provide information up to November 2023, so any subsequent developments are not reflected in this analysis.**
# > 
# > **Overall, Apple's SEC filings portray a company that has navigated a challenging and competitive landscape to become one of the most valuable and influential technology companies in the world. While challenges and uncertainties remain, Apple's strong financial position, focus on innovation, and loyal customer base suggest continued success in the years to come.**
# 

