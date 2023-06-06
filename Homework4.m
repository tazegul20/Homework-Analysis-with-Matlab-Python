
%solution_2 /A_for
A = zeros(5, 8);
for i = 1:5
    for j = 1:8
        if i > j
            A(i, j) = 4*i - 2*j;
        end
        if i <= j
            A(i, j) = i^2 - 3*j;
        end
    end
end
%solution_2 /A_while
A = zeros(5, 8);

i = 1;
j = 1;

while i <= 5
    j = 1;
    while j <= 8
        if i > j
            A(i, j) = 4*i - 2*j;
        end
        if i <= j
            A(i, j) = i^2 - 3*j;
        end
        j =+ 1;
    end
    i =+ 1;
end

%solution_3
n = 5;

x = 2;

terms = zeros(1, n+1);

for j = 0:n

terms(j+1)=(abs(x).^j)/factorial(j);
end
termsSum = sum(terms);

t = exp(x);

y = termsSum.^sign(x);

h = abs(t-y);

display(y);

display(h);

 
n = 15;

x = 2;

terms = zeros(1, n+1);
for j = 0:n
terms(j+1)=(abs(x).^j)/factorial(j);
end
termsSum = sum(terms);
t = exp(x);
y = termsSum.^sign(x);
h = abs(t-y);
display(y);
display(h);
n = 15;
x = 2;
terms = zeros(1, n+1);
for j = 0:n
terms(j+1)=(abs(x).^j)/factorial(j);
end
termsSum = sum(terms);
t = exp(x);
y = termsSum.^sign(x);
h = abs(t-y);
display(y);
display(h);


%solution_4
T=200;
rng('default');
u=randn(1,T);
t=1:T;
y=zeros(1,length(T));
for i=2:T
y(1,i)=y(1,i-1) + u(1,i-1);
end
plot(t,y)
axis([0 200 -5 20])
grid

rng('default');
T=200;
u2=randn(1,T);
t=1:T;
ro=0.7;
y2=zeros(1,length(T));
for j=2:T
y2(1,j)=ro*y2(1,j-1) + u2(1,j-1);
end
hold on
plot(t,y2,'r');
axis([0 200 -5 20]);
grid;

%solution_5
Grade = input('Enter Letter grade :','s');
if Grade == 'A+'
    fprintf('Equivalent Grade point is 4\n');
else
    if Grade =='A'
        fprintf('Equivalent Grade point is 4.0\n');
    else
        if Grade=='A-'
            fprintf('Equivalent Grade point is 3.7\n');
        else
            if Grade =='B+'
                fprintf('Equivalent Grade point is 3.3\n');
            else
                if Grade=='B'
                    fprintf('Equivalent Grade point is 3.0\n');
                else
                    if Grade=='B-'
                        fprintf('Equivalent Grade point is 2.7\n');
                    else
                        if Grade=='C+'
                            fprintf('Equivalent Grade point is 2.3\n');
                        else
                            if Grade == 'C'
                                fprintf('Equivalent Grade point is 2.0\n');
                            else
                                if Grade =='C-'
                                    fprintf('Equivalent Grade point is 1.7\n');
                                else
                                    if Grade=='D+'
                                         fprintf('Equivalent Grade point is 1.3\n');
                                    else
                                        if Grade=='D'
                                             fprintf('Equivalent Grade point is 1.0\n');
                                        else
                                            if Grade=='F'
                                                 fprintf('Equivalent Grade point is 0\n');
                                            else
                                                fprintf('Error !!');
                                            end
                                        end
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
end
%solution_6
Grade = input('Enter Letter grade :','s');
switch Grade
    case A+
        fprintf('Equivalent Grade point is 4 \n');
    case A
        fprintf('Equivalent Grade point is 4.0\n');
    case A-
        fprintf('Equivalent Grade point is 3.7\n');
    case B+
        fprintf('Equivalent Grade point is 3.3\n');
    case B
        fprintf('Equivalent Grade point is 3.0 \n');
    case B-
        fprintf('Equivalent Grade point is 2.7\n');
    case C+
        fprintf('Equivalent Grade point is 2.3\n');
    case C
        fprintf('Equivalent Grade point is 2.0\n');
    case C-
        fprintf('Equivalent Grade point is 1.7 \n');
    case D+
        fprintf('Equivalent Grade point is 1.3\n');
    case D
        fprintf('Equivalent Grade point is 1.0\n');
    case F
        fprintf('Equivalent Grade point is 0.0\n');        
    otherwise
        fprintf('ERORRR');
end
 
    
%solution_7
rng('default');
x = 0:0.05:10;
n = length(x);
y = cos(x) + 0.3*normrnd(0,1,[1,n]);


y1=zeros(length(y),1);
y2=zeros(length(y),1);



for i=2:length(x)-1
y1(i)=(y(i-1)+y(i)+y(i+1))/3;
end



for i=3:length(x)-2
y2(i)=(y(i-2)+2*y(i-1)+3*y(i)+2*y(i+1)+y(i+2))/5;
end


plot(x,y); hold on
plot(x,y1);
plot(x,y2);
hold off
legend('Original Data','q7_Rectangular(m=3)','q7_Triangular(m=5)');

%solution_8
rng default
V=chi2rnd(3,[1,10]);
count=length(V);
V;
for j=1:1:count-1

for i=1:1:count-1

if V(i)<V(i+1) 

temporary=V(i);

V(i)=V(i+1);

V(i+1)=temporary;

end

end

end