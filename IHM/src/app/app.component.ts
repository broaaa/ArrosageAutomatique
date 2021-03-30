import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  title: string = 'Bwaaa garden app';
  herbeStatus: string = 'off'
  potagerStatus: string = 'off'
  log: string;
  time: number = 5;
  timeValue: string = "Minutes"

  constructor(public api: ApiService) { }

  ngOnInit(): void {
    this.getStatus();
  }

  handleHerbe() {
    if (!this.checkTime())
      return;
    this.api.postHerbe(this.time)
      .then(res => {
        this.log = JSON.stringify(res);
        this.herbeStatus = 'on';
      }).catch(err => {
        this.herbeStatus = 'off';
        this.log = err;
        console.log('error when calling api:' + err);
      });
  }

  checkTime() {
    if (this.time < 1) {
      console.log("bad Time");
      this.log = 'badtime';
      return false;
    }
    this.log = '';
    return true;
  }

  handlePotager() {
    if (!this.checkTime())
      return;
    this.api.postPotager(this.time)
      .then(res => {
        this.log = JSON.stringify(res);
        this.potagerStatus = 'on';
      }).catch(err => {
        this.potagerStatus = 'off';
        this.log = err;
        console.log('error when calling api:' + err);
      });
  }

  handleStop() {
    this.api.postStop().then(res => {
      this.herbeStatus = res.herbe['2'];
      this.potagerStatus = res.potager['4'];
      console.log('herbe=' + this.herbeStatus + '   potager=' + this.potagerStatus);
    }).catch(err => {
      this.log = err;
      console.log(err);
    });
  }

  getStatus() {
    console.log("here")
    this.api.getStatus().then(res => {
      this.herbeStatus = res.herbe['2'];
      this.potagerStatus = res.potager['4'];
      console.log('herbe=' + this.herbeStatus + '   potager=' + this.potagerStatus);
    }).catch(err => {
      this.log = err;
      console.log(err);
    });
  }
}
