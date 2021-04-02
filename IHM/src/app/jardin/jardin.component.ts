import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-jardin',
  templateUrl: './jardin.component.html',
  styleUrls: ['./jardin.component.css']
})
export class JardinComponent implements OnInit {
  time: number = 1;
  herbeStatus: string = 'off';
  potagerStatus: string = 'off';
  log: string;

  constructor(public api: ApiService) { }

  ngOnInit() {
    console.log('on jardin');
    this.getStatus();
  }

  valueChanged(e) {
    this.time = e.target.value;
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

  checkTime() {
    if (this.time < 1) {
      console.log("bad Time");
      this.log = 'badtime';
      return false;
    }
    this.log = '';
    return true;
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

}
