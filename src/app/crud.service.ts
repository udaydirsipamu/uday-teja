import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Book } from './Book';

@Injectable({
  providedIn: 'root'
})
export class CRUDService {
  /**baseURL="http://localhost:3000/Books";**/
  baseURL="http://localhost:5000/book"
  constructor(private httpClient : HttpClient) { }
  getBooks():Observable<any>{
    return this.httpClient.get(this.baseURL);
  }
  insertBook(book:Book):Observable<any>{
    //return(this.httpClient.post(this.baseURL,book));
    return (this.httpClient.post(this.baseURL+"/"+book.id,book));
  }
  updateBook(book:Book):Observable<any>{
    let updateURL=this.baseURL + "/" + book.id;
    return(this.httpClient.put(updateURL,book));
  }
  deleteBook(book_id:number):Observable<any>{
    let deleteURL=this.baseURL + "/" + book_id;
    alert("Delete URL: " + deleteURL)
    return this.httpClient.delete(deleteURL);
  }
}
