def get_define(self):
    try:
        dfn = self.soup.find('div', attrs = {'data-dobid':'dfn'}).text
        return dfn
    except:
        return 'define not found'


def get_synonyms(self):
    try:
        synonym = self.soup.find('table', attrs={'class': 'vk_tbl vk_gy'}).text.split(' ')
        synonym = ' '.join(synonym[:4])
        return synonym
    except:
        return 'synonyms not found'

def get_example(self):
    try:

        for ex in self.soup.find('span', attrs={'class': 'vmod'}).div:
            print('example: ' + ex)
    except:
        pass


def get_type(self):
    try:
        type = self.soup.find('div', attrs = {'class':'lr_dct_sf_h'}).text
        return type

    except:
        return 'cant found type'

def get_all(self):
    try:
        all = self.soup.find('ol',attrs = {'class':'lr_dct_sf_sens'})
        define = '\n\n'.join([li.text for li in all.findAll('li')][1:])
        return define

    except:
        return 'nothing found'
