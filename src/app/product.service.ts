import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }

  LaptopList=[
    {"product_id":101,"product_name":"TV","description":"LG","cost":35000},
    {"product_id":102,"product_name":"Mobile","description":"Samsung","cost":35000},
    {"product_id":103,"product_name":"Laptop","description":"HP","cost":55000},
    {"product_id":104,"product_name":"Earphones","description":"Boat","cost":5000},
    {"product_id":105,"product_name":"Speakers","description":"Dolby digital","cost":15000}
  ]
    getLaptopList(){
      return this.LaptopList
    }
}
