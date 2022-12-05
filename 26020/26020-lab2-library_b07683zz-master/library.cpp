/* complete this file */
#include<iostream>
#include <fstream>
#include <string>
#include<cstring>
#include"library.h"


void Document::updateTitle(const char *newTitle){
    _title=new char[strlen(newTitle)];
    strcpy(_title,newTitle);
}
void Document::updateYear(int newYear){
    _year=newYear;
}
void Document::updateQuantity(int newQuantity){
    _quantity=newQuantity;
}
char * Document::getTitle(){
    
    return _title;

}

int Document::getYear(){

    return _year;
}
int Document::getQuantity(){
    return _quantity;
}

/* Used when someone tries to borrow a document, should return 0 on success
    * and something else on failure */
int Document::borrowDoc(){
    if(_quantity>0){
        _quantity--;
        return 0;
    }else{
        return -1;
    }
    return 0;

}

/* Used when someone returns a document */
void Document::returnDoc(){
    _quantity++;
}


 Novel::Novel(const char *title, const char *author, int year, int quantity){
     updateTitle(title);
     updateAuthor(author);
     updateYear(year);
     updateQuantity(quantity);
 }
Novel::~Novel(){
     delete _author;
}
void Novel::print(){
    cout<<"Novel, title: "<<getTitle()<<", author: "<<getAuthor()<<", year: "<<getYear()<<", quantity: "<<getQuantity()<<""<<endl;
}
document_type Novel::getDocType(){
    return DOC_NOVEL;
}
 /* getters and setters */
void Novel::updateAuthor(const char *newAuthor){
    _author=new char[strlen(newAuthor)];
     strcpy(_author,newAuthor);
}
char *Novel::getAuthor(){
    return _author;
}








Comic::Comic(const char *title, const char *author, int issue, int year, int quantity){
    updateTitle(title);
    updateAuthor(author);
    updateYear(year);
    updateQuantity(quantity);
    updateIssue(issue);
}
Comic::~Comic(){
    delete _author;
}

void Comic::print(){
    cout<<"Comic, title: "<<getTitle()<<", author: "<<getAuthor()<<", issue: "<<getIssue()<<", year: "<<getYear()<<", quantity: "<<getQuantity()<<""<<endl;
}
document_type Comic::getDocType(){
return DOC_COMIC;
}
/* getters, setters */
void Comic::updateAuthor(const char *newAuthor){
    _author=new char[strlen(newAuthor)];
     strcpy(_author,newAuthor);
}
void Comic::updateIssue(int newIssue){
    _issue=newIssue;
}
char *Comic::getAuthor(){
    return _author;
}
int Comic::getIssue(){
    return _issue;
}



Magazine::Magazine(const char *title, int issue, int year, int quantity){
    updateTitle(title);
    updateYear(year);
    updateQuantity(quantity);
    updateIssue(issue);
}
Magazine::~Magazine(){

}
document_type Magazine::getDocType(){
    return DOC_MAGAZINE;
}
void Magazine::print(){
    cout<<"Magazine, title: "<<getTitle()<<", issue: "<<getIssue()<<", year: "<<getYear()<<", quantity: "<<getQuantity()<<""<<endl;
}

/* getters, setters */
void Magazine::updateIssue(int newIssue){
    _issue=newIssue;
}
int Magazine::getIssue(){
    return _issue;
}













Library::Library(){

}

/* print the entire library on the standard output, one line per document,
    * in the order they were inserted in the library, using the print()
    * methods implemented by the document objects */
void Library::print(){
    for(auto it:_docs){
        it->print();
    }
}

/* Dump the library in CSV format in a file, the format is: 1 line per
    * file:
    * <document type>,<title>,<author>,<issue>,<year>,<quantity>
    * A field not relevant for a given document type (e.g. issue for novel)
    * should be left blank. Return 0 on success, something else on failure.
    * Here you should use low-level file I/Os (open, write, etc.) as seen
    * in the course. */
int Library::dumpCSV(const char *filename){
    ofstream outfile(filename, ios::trunc);
    for(auto p:_docs){
        if(p->getDocType()==DOC_NOVEL){
            auto it=(dynamic_cast<Novel*>(p));
            outfile<<"novel,"<<it->getTitle()<<","<<it->getAuthor()<<",,"<<it->getYear()<<","<<it->getQuantity()<<endl;
        }else if(p->getDocType()==DOC_MAGAZINE){
            
             auto it=(dynamic_cast<Magazine*>(p));
            outfile<<"magazine,"<<it->getTitle()<<",,"<<it->getIssue()<<","<<it->getYear()<<","<<it->getQuantity()<<endl;
        }else{
            
             auto it=(dynamic_cast<Comic*>(p));
            outfile<<"comic,"<<it->getTitle()<<","<<it->getAuthor()<<","<<it->getIssue()<<","<<it->getYear()<<","<<it->getQuantity()<<endl;
        }
        
    }
    outfile.close();
    return 0;

}

/* search for a document in the library, based on the title. We assume that
    * a title identify uniquely a document in the library, i.e. there cannote
    * be 2 documents with the same title Returns a pointer to the document if
    * found, NULL otherwise */
Document *Library::searchDocument(const char *title){
    for(auto it:_docs){
        if(strcmp(it->getTitle(),title)==0){
            return it;
        }
      
    }
    return nullptr;
}

/* Add/delete a document to/from the library, return 0 on success and
    * something else on failure.  */
int Library::addDocument(Document *d){

    _docs.push_back(d);
    return 0;

}
int Library::delDocument(const char *title){
    int i=0;
    for(auto it:_docs){
        if(strcmp(it->getTitle(),title)==0){
            _docs.erase(_docs.begin()+i);
            return 0;
        }
      i++;
    }
    return -1;

}

/* Count the number of document of a given type present in the library */
int Library::countDocumentOfType(document_type t){
    int sum=0;
    for(auto it:_docs){
        if(it->getDocType()==t){
            sum++;
        }
    }
    
    return sum;

}

/* Borrow/return documents, return 0 on success, something else on
    * failure */
int Library::borrowDoc(const char *title){
    auto it=searchDocument(title);
    if(it!=nullptr){

        return it->borrowDoc();
        
    }
    return -1;
    

}
int Library::returnDoc(const char *title){

    auto it=searchDocument(title);
    if(it!=nullptr){
        it->returnDoc();
        return 0;
       
    }
    return -1;
}