import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  constructor(private http: HttpClient) {}

  askChat(text: string): Promise<{ respuesta: any }> {
    return this.http
      .get<{ respuesta: string }>(environment.url + '/chat', {
        params: new HttpParams().append('frase', text),
      })
      .toPromise();
  }

  create(codigo: number, nombre: string): Promise<{ respuesta: string }> {
    return this.http
      .get<{ respuesta: string }>(environment.url + '/create', {
        params: new HttpParams().append('nombre', nombre).append('codigo', codigo),
      })
      .toPromise();
  }
}
