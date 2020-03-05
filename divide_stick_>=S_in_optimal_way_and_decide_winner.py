'''   Two sweet dogs, Bernard and Havanese, play the following game.
There are P sticks, each of exactly Q meters in length. The dogs move in turns. For each move a dog chooses a stick and splits it into two or more equal parts each having integer length greater than or equal to S meters. Each resulting part is also a stick. The dog that can't make a move loses. Thus, the other dog wins.
Bernard makes the first move. Now you have to determine the winner if players play in the optimal way.

Input :
First line of Input contains number of test cases T. Each test case contains three integers P, Q and S.

Output :
For each test case print "Bernard", if Bernard wins, or "Havanese", if Havanese wins. You should print everything without the quotes.

Constraint:
1 ≤ T ≤ 10
1 ≤ P,Q,S ≤ 109
SAMPLE INPUT

2
1 15 4
4 9 5

SAMPLE OUTPUT

Bernard
Havanese

Time Limit: 1.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed Languages: Bash, C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, R(RScript), Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic
   '''

#Solutin in C++
#I didn't solved it 

    #include <bits/stdc++.h>
     
    using namespace std;
     
    int main() {
        ios::sync_with_stdio(0);
        
        int t;
        cin >> t;
        for (int z = 1; z <= t; z++) {
            int p, q, s;
            cin >> p >> q >> s;
            if (p % 2 == 0) {
                cout << "Havanese\n";
                continue;
            }
            int m = sqrt(q);
            bool win = 0;
            for (int i = 2; i <= m; i++) {
                if (q % i == 0) {
                    if (q / i >= s) {
                        win = 1;
                    }
                }
            }
            if (s == 1 && q > 1) win = 1;
            if (win) cout << "Bernard\n";
            else cout << "Havanese\n";
        }
        return 0;
        
    }

#Solution in C lang

    #include <stdio.h>
     
    int func(int i, int s, int q){
        
        int j = (i >=s && i!= q);
        return j;
    }
     
    int func2(int q, int s){
        
        for(int i=1; i*i <=q; i++)
        {
            if(q%i ==0 && (func (i,s,q) || func (q / i,s,q)))
                return 1;
        }
        return 0;
    }
     
    int main(){
        
        int t;
        scanf("%d",&t);
        
        while(t>0)
        {
            int p,q,s;
            scanf("%d %d %d",&p,&q,&s);
            
            if(p%2 !=0 && func2(q,s))
                printf("Bernard\n");
            else
                printf("Havanese\n");
                
            t--;
        }
        return 0;
    }


#Solution in Python

n=int(input())
for k in range(n):
    p, q, s=map(int, input().split())
    if p%2==0:
        print("Havanese")
    else:
        d=set()
        i=1
        while i*i<=q:
            if q%i==0:
                d.add(i)
                d.add(q/i)
            i+=1
        f=1
        for i in d:
            if i>=s and i<q:
                print("Bernard")
                f=0
                break
        if f:
            print("Havanese")

#Other solutions in python

T = int(input())
for i in range(0,T):
    P,Q,S =input().split()
    p = int(P)
    q = int(Q)
    s = int(S)
    flg_p = 'N'
    max_fact = int(q**0.5)
    for i in range(2,max_fact+2):
        if q == 1:
            flg_p = 'Y'
            print ('Havanese')
            break
        if s == 1:
            flg_p = 'Y'
            if p%2 == 0:
                print('Havanese')
            else:
                print ('Bernard')
            break
 
        if (q%i) == 0 and (q/i)>= s:
            flg_p = 'Y'
            if p%2 == 0:
                print('Havanese')
            else:
                print ('Bernard')
            break
        elif (q%i) == 0 and (q/i) < s:
            flg_p = 'Y'
            print ('Havanese')
            break
    if flg_p == 'N':
        print ('Havanese')

##################################################

    t=int(input())
    for _ in range(t):
        p,q,s=map(int, input().split())
        if(p%2==0):
            print("Havanese")
        else:
            l=[]
            i=1
            while(i**2<=q):
                if(q%i==0):
                    l.append(i)
                    l.append(q/i)
                i=i+1
            l=list(set(l))
            f=0
            for i in l:
                if(i>=s):
                    if(i<q):
                        print("Bernard")
                        f=1
                        break
            if(f==0):
                print("Havanese")

################################################################


    def div(n):
    	from math import sqrt
    	s = int(sqrt(n + 0.0))
    	t = []
    	for i in range(1, s + 1):
    		if n % i == 0:
    			t.append(i)
    			t.append(n / i)
    	return t
     
    def win(p, q, s):
    	if p % 2 == 0:
    		return False
    	
    	for d in div(q):
    		if d >= 2 and q / d >= s and not win(d, q / d, s):
    			return True
    			
    	return False
     
    T = int(input())
    for t in range(T):
    	p, q, s = map(int, input().split())
    	if win(p, q, s):
    	    print("Bernard")
    	else:
    	    print("Havanese")




