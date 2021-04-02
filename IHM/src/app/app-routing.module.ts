import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { JardinComponent } from './jardin/jardin.component'
import { VoletsComponent } from './volets/volets.component'


const routes: Routes = [
  { path: 'jardin', component: JardinComponent },
  { path: 'volet', component: VoletsComponent },
  { path: '', redirectTo: '/jardin', pathMatch: 'full' },
  { path: '**', component: JardinComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
