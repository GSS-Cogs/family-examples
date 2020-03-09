# ## IMPORTANT
#
# Totally fake transform. We're just using pre-prepared csv and an entirely fake scraper. We're literally just getting the data onto the platform as quickly as possible.

# +

from gssutils import *
from gssutils.metadata import Distribution

# Create a temporary scraper
def temp_scrape(scraper, tree):
    scraper.dataset.title = "NHD Digital Example Data"
    dist = Distribution(scraper)
    dist.title = 'A distribution'
    dist.downloadURL = 'foo'
    dist.mediaType = ODS
    scraper.distributions.append(dist)
    scraper.dataset.publisher = 'https://www.gov.uk/government/organisations/nhs-digital'
    scraper.dataset.description = "An example dataset created from the 'Patients Registered at a GP Practice - December 2019: Single year of age' dataset, both male and female combined. For the sake of this example we've used only agres 35 and below."
    return

scrapers.scraper_list = [('http://www.fake.com', temp_scrape)]
scraper = Scraper('http://www.fake.com')
scraper

# +
tidy_data = pd.read_csv("combined_source.csv")

# Output observations file
destinationFolder = Path('out')
destinationFolder.mkdir(exist_ok=True)
tidy_data.to_csv("out/observations.csv", index=False)

# Trig and metadata
with open(destinationFolder / f'observations.csv-metadata.trig', 'wb') as metadata:
    metadata.write(scraper.generate_trig())

csvw = CSVWMetadata('https://gss-cogs.github.io/family-examples/reference/')
csvw.create(destinationFolder / 'observations.csv', destinationFolder / 'observations.csv-schema.json')
# -




