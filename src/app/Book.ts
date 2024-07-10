export class Book{
    id:number=0;
    title:String="";
    author:String="";
    cost:number=0;
    constructor(id:number,title:String,author:String,cost:number){
        this.id=id;
        this.title=title;
        this.author=author;
        this.cost=cost;
    }
}