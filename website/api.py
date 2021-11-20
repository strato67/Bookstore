import wikipediaapi
import json
from . import db
from .models import Book


class infoQuery():

    def info(booktitle):
        wiki = wikipediaapi.Wikipedia('en')
        pageSearch = wiki.page(booktitle)

        if pageSearch.exists() == True:
                descJSON = json.dumps({'description':pageSearch.summary})
                descJSON = descJSON.replace('\\n','')
                return(descJSON)
        else:
                return "No information available"


'''
        page_py = wiki.page(test)
        print(page_py)


        print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

        page_missing = wiki.page('NonExistingPageWithStrangeName')
        print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

#print("Page - Summary: %s" % page_py.summary)


        initial = {'description':page_py.summary}
        initial = json.dumps(initial)
        final_dictionary = json.loads(initial)

        print(final_dictionary)
        
'''