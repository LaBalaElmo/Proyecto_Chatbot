import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
import { ChatService } from '../services/chat.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  name = '';
  code = '';

  constructor(
    private navCtrl: NavController,
    private service: ChatService) {}

  ngOnInit() {}

  async login() {
    console.log(this.name);
    console.log(this.code);

    //si todo ok
    localStorage.setItem('name', this.name);
    localStorage.setItem('code', this.code);
    this.navCtrl.navigateForward('/home');
    const aux = await this.service.create(+this.code, this.name)
    console.log(aux.respuesta);
  }
}
