'''
Created on 2012. 7. 31.

@author: S33416
'''

class pagingHelper:
    "paging helper class"
    def getTotalPage(self, total_cnt, rowsPerPage):
        #self.total_pages = 0;
        
        if ((total_cnt % rowsPerPage) == 0):
            self.total_pages = total_cnt / rowsPerPage;
        else:
            self.total_pages = (total_cnt / rowsPerPage) + 1;
        
        return self.total_pages;        

    def __init__(self ):
        self.total_pages = 0;
        
        