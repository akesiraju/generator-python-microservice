class Config():
    def __init__(self):
        self.cfg = {
            'docs': {
                'public_swagger_url': 'http://localhost:<%= PORT %>/v1/docs/private'
            }
        }

    def get_section(self, section_name):
        return self.cfg[section_name]
