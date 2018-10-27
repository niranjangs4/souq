import os
package = os.path.join(os.getcwd().rsplit('\\',1)[0],'output')


output_config = dict(json_file=os.path.join(package,'perfumes.json'),
                     pages=os.path.join(package,"page.txt"),
                     jsonreport=os.path.join(package,"report_perfumes.json"),
                     product=os.path.join(package,"product.txt"),
                     csv_file=os.path.join(package,"PerfumeReport.csv"),
                     results=package,
                     product_link=r'https://saudi.souq.com/sa-en/souq--shop/perfumes---and---fragrances-478/a-t/s/?seller=souq-shop&rpp=50&page=2')

