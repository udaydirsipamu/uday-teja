export class Appointments{
    id:number=0;
    name:String="";
    service:String="";
    date:String="";
    time:String="";

    constructor(id:number,name:String,service:String,date:String,time:String){
        this.id=id;
        this.name=name;
        this.service=service;
        this.date=date;
        this.time=time
    }
}