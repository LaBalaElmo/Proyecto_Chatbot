import { NavController } from '@ionic/angular';
import { Message } from './../model/message.model';
import { Component } from '@angular/core';
import { ChatService } from '../services/chat.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  msgList: Message[] = [
  ];
  me = 'me';
  input = '';
  constructor(private navCtrl: NavController, private service: ChatService) {}

  async sendMessage() {
    console.log(await this.service.askChat(this.input));
    this.msgList.push({
      from: "me",
      msg: this.input,
      created: new Date().getHours()
    });
    this.msgList.push({
      from: 'XhatButt',
      msg: (await this.service.askChat(this.input)).respuesta,
      created: new Date().getHours()
    })
    this.input = '';
  }

  logout() {
    localStorage.removeItem('name');
    localStorage.removeItem('code');
    this.navCtrl.navigateForward('/login');
  }
}
