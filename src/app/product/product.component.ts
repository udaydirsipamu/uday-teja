import { Component } from '@angular/core';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrl: './product.component.css'
})
export class ProductComponent {
  constructor(private productService : ProductService){}
  laptoplist : any =[]
  bDisplayLaptopData : boolean = false

  ngOnInit(){
    this.laptoplist=this.productService.getLaptopList()
  }

  enableLaptopFlag(){
    this.bDisplayLaptopData = true
  }
}
