import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VoletsComponent } from './volets.component';

describe('VoletsComponent', () => {
  let component: VoletsComponent;
  let fixture: ComponentFixture<VoletsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VoletsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VoletsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
