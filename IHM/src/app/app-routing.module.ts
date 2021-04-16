import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { JardinComponent } from './jardin/jardin.component'
import { VoletsComponent } from './volets/volets.component'


const routes: Routes = [
  { path: 'jardin', component: JardinComponent },
  { path: 'volets', component: VoletsComponent },
  { path: '', redirectTo: '/jardin', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
