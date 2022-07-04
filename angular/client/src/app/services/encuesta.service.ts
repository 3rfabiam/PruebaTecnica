import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EncuestaService {

  private BASE_URL = "http://localhost:5000/"; 

  constructor(private http: HttpClient) {
    console.log('Servio persona');
  }
  getDatos():Observable<any>{

    return this.http.get(`${this.BASE_URL}/encuesta`)
    
  }

  crearDatos(usuario:Object):Observable<any>{
    return this.http.post(`${this.BASE_URL}/encuesta`,usuario)
  }


}
