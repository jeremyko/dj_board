# -*- coding: utf-8 -*-
# Create your views here.
#from django.template.loader import get_template  
#from django.template import Template, Context  
#from django.http import Http404, HttpResponse  
from django.shortcuts import render_to_response
from django.utils import timezone
from sample_board.models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponseRedirect

# 한글!!
#===========================================================================================
def home(request):    
    boardList = DjangoBoard.objects.order_by('-id')[0:5]  
    # DjangoBoard.objects.all()        
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': boardList.count(), 'current_page':1 } )
    
#===========================================================================================
def show_write_form(request):
    return render_to_response('writeBoard.html')  

#===========================================================================================
@csrf_exempt
def DoWriteBoard(request):
    br = DjangoBoard (subject = request.POST['dbsubject'],
                      name = request.POST['dbname'],
                      mail = request.POST['dbemail'],
                      memo = request.POST['dbmemo'],
                      created_date = timezone.now()
                     )
    br.save()
    
    # 다시 조회
    boardList = DjangoBoard.objects.order_by('id')[0:5]  
    # DjangoBoard.objects.all()        
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': boardList.count(), 'current_page':1 } )        

#===========================================================================================
def viewWork(request):
    pk= request.GET['memo_id']    
    #print 'pk='+ pk
    boardData = DjangoBoard.objects.get(id=pk)
    #print boardData.memo  
    return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'], 
                                                'current_page':request.GET['current_page'], 
                                                'searchStr': request.GET['searchStr'], 
                                                'boardData': boardData } )            
   
#===========================================================================================
def listSpecificPageWork(request):    
    current_page = request.GET['current_page']
    totalCnt = DjangoBoard.objects.all().count()                  
    
    print 'current_page='+current_page
    print  totalCnt
    
    # 페이지를 가지고 범위 데이터를 조회한다 => raw SQL 사용함
    # page출력이 반대순서로 되고 있음!
    rowsPerPage = 2    
    boardList = DjangoBoard.objects.raw('SELECT * FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS, ceil( rownum / %s ) as page    \
                                        FROM SAMPLE_BOARD_DJANGOBOARD  ORDER BY ID DESC ) WHERE page = %s', [rowsPerPage, current_page])
    
    print  boardList
    return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 'current_page':current_page } )












'''
final String SELECT_PAGE = "SELECT * FROM (    SELECT    ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS, ceil( rownum / #{rowsPerPage} ) as page "+
            "FROM SAMPLE_BOARD_DJANGOBOARD  ORDER BY ID DESC ) WHERE page = #{page}";
    
    final String SELECT_BY_ID = "SELECT ID,SUBJECT,NAME,CREATED_DATE,MAIL,MEMO,HITS from SAMPLE_BOARD_DJANGOBOARD WHERE ID=#{id}";
    
    //  '%#{searchThis}%' 로 사용시 에러! java.sql.SQLException: 부적합한 열 인덱스
    final String SELECT_CNT_BY_SUBJECT = "SELECT COUNT(1) FROM SAMPLE_BOARD_DJANGOBOARD WHERE SUBJECT LIKE '%'||'${searchThis}'||'%'";
        
    final String SELECT_ROWS_BY_SUBJECT = "SELECT * FROM (SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS, "+
            "ceil( rownum / #{rowsPerPage}) as page FROM SAMPLE_BOARD_DJANGOBOARD  WHERE SUBJECT LIKE '%'||'${likeThis}'||'%' ORDER BY ID DESC ) WHERE page = #{page}";
        
    final String SELECT_CNT_ALL = "SELECT count(1) FROM SAMPLE_BOARD_DJANGOBOARD";
'''


