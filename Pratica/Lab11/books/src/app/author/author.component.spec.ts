import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AuthorsComponent } from './author.component';

describe('AuthorComponent', () => {
  let component: AuthorsComponent;
  let fixture: ComponentFixture<AuthorsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AuthorsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AuthorsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
