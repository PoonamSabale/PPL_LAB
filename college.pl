% courses in department

dept_course(comp_dept,dsa).
dept_course(comp_dept,ppl).
dept_course(comp_dept,dsgt).
dept_course(comp_dept,dld).
dept_course(math_dept,la).
dept_course(math_dept,ode).
dept_course(math_dept,uvc).


% departments having students

dept_student(comp_dept,tnb).
dept_student(math_dept,tnb).
dept_student(comp_dept,ssd).
dept_student(math_dept,ssd).
dept_student(comp_dept,pas).
dept_student(math_dept,pas).
dept_student(comp_dept,gvd).
dept_student(math_dept,gvd).


% faculty teaches these courses

faculty_course(vkk,ppl).
faculty_course(vvk,dsgt).
faculty_course(pfp,dld).
faculty_course(spk,dsa).
faculty_course(dng,la).
faculty_course(jtm,ode).
faculty_course(jtm,uvc).


% faculties in department
dept_faculty(D,F):-dept_course(Z,C),faculty_course(D,S).


% courses taken by students

student_course(S,C):-dept_student(Z,S),dept_course(Z,C).

% faculty teaches these students

faculty_student(F,S):-dept_student(Z,S),dept_course(Z,C),faculty_course(F,C).
