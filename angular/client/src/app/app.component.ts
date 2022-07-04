import { Component } from '@angular/core';
import { EncuestaService } from './services/encuesta.service';
import { Usuario } from './modelos/usuario';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';
  public encuestas:Array<any> = [];

  constructor(
    private encuestaService: EncuestaService) {
      this.encuestaService.getDatos().subscribe(resp =>{
        console.log(resp.encuesta[0].Favorita)
      })
    }

    ngOnInit():void {
      this.encuestaService.getDatos()
      .subscribe((resp: any)=>{
        this.encuestas = resp
      })
    }

    selectedUsuario:Usuario = new Usuario();
    seleccionar(persona:Usuario){
      this.selectedUsuario = persona;
      console.log(this.selectedUsuario);
    }

    guardar(){
      this.encuestaService.crearDatos(this.selectedUsuario).subscribe();
  }

}
