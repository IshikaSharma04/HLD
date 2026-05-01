# Why We Learned DSA  let us see                       
                  
DSA (Data Structures and Algorithms) is mainly used to optimized code performance.               
                   
Optimization is done in terms of:                     
- Time Complexity → how fast the code runs                    
- Space Complexity → how much memory the code uses                
                     
That is the main focus of DSA.                           
---                         
                       
# Low Level Design (LLD)                   
    
Whether code is:               
- maintainable,             
- extensible,   
- easy to modify        
     
depends on the Low Level Design of the code.     
    
In LLD, we focus on: 
- structure of classes, 
- inheritance,
- interfaces,
- design patterns,
- overall code organization.

---

# Moving Beyond LLD → System Design 

Now we “zoom out” further.

Instead of focusing only on code structure, we focus on:
- how the application is deployed,
- how it remains available,
- how it scales for many users.

Questions addressed in System Design:
- If multiple users send requests simultaneously, how do we handle them?
- How do we reduce latency?
- How do we make the system scalable and highly available?

---

# Latency

Latency = the time taken by a system/API to return a response after a request is sent.

Lower latency = better performance.

---

# Important Interview Example

Google Staff Engineer interview question:

"Given a file containing words, sort all the words alphabetically."

Initially, this seems easy:
1. Read the file
2. Load data from hard disk to RAM
3. Store words in an ArrayList
4. Use Collections.sort()

But requirement clarification is important.

---

# Actual Requirement

The file size is:

# 1 Petabyte (PB)

Storage units:
- 1 MB = 10^6 B
- 1 GB = 10^9 B
- 1 TB = 10^12 B
- 1 PB = 10^15 B

At this scale, normal sorting approaches fail because the entire data cannot fit into RAM.

Main lesson:
Always clarify requirements before deciding the solution.

# Why the Earlier Approach Will Not Work

The previous approach will not work for 1 Petabyte of data because:

- We do not have enough RAM to load all the data.
- Even storing 1 PB in a single hard disk is extremely expensive.

So, the data is distributed across multiple servers. 

---

# Distributed Data

Different servers store different parts of the data.

Example:
- Server 1 → some portion of data
- Server 2 → another portion
- Server 3 → remaining portion

The data becomes fragmented across machines.

---

# New Challenges Introduced

Now the problem is no longer just “sorting data”.

We must handle distributed system challenges.

---

# 1. Reading Distributed Data

Question:
How do we read data when it is fragmented across multiple machines?

Possible approach:
- Read data from one machine at a time
- Sort chunks individually
- Merge the sorted data later
- Redistribute the final sorted data

---

# 2. Data Issues

Possible problems:
- Data corruption
- Hard disk damage
- Missing data blocks

A server or storage device may fail at any time.

---

# 3. Server-Related Issues

All servers may not have the same configuration.

Example:
- One server may have 50 GB RAM
- Another may have only 2 GB RAM

Different RAM/storage capacities can cause: 
- uneven workload distribution,
- bottlenecks,
- inefficient algorithms.

This can highly unoptimize the system.

---

# 4. Network Issues

Since machines communicate over a network, problems like:
- network lag,
- slow communication,
- packet loss,
- connection failures

can affect the system.

If the network becomes slow, the entire distributed operation slows down.

---

# Main Problems Addressed in System Design

System Design mainly deals with:

- Data-related issues
- Server-related issues
- Network-related issues

and how to build systems that can still work efficiently despite these problems.


# Problem of Remembering URLs

Earlier, remembering long website URLs was difficult.

People often used to:
- write URLs in notebooks/books,
- save them manually for later use.

Joshua saw this as an opportunity and created a website where users could:
- log in,
- save bookmarks/URLs online.

---

# Database Storage Discussion

Suppose we store bookmark data in tables.

To design the database properly, we first need to calculate:
- memory required per row.

Example:
- `id` field → integer
- Integer size = 4 bytes

But 4 bytes may not always be enough.

Example:
- When "Gangnam Style" crossed 1 billion views,
- 4-byte limitations became important in large-scale systems.

So larger datatypes like:
- 8-byte integers (`long`)
may be needed.

---

# URL Storage Size

A URL can be large.

Approximation:
- URL size ≈ 1000 bytes
- ≈ 1 KB per URL

When millions of users store bookmarks, storage grows rapidly.

---

# Single Server Problem

Suppose initially:
- server storage = 40 GB

This may only last for a limited time.

A temporary solution:
- upgrade to a larger server,
- example: 500 GB server.

But eventually the same problem occurs again.

This is called a scalability problem.

---

# Solution → Multiple Servers

Instead of storing all data on one server:
- distribute data across multiple servers.

But this introduces new questions:
- How should data be divided?
- Which server stores which data?
- How do users reach the correct server?

---

# DNS and IP Address Mapping

Computers do not understand domain names directly.

They understand:
- IP addresses.

DNS (Domain Name System) maintains mapping between:
- domain names
- IP addresses.

Example:
google.com → IP address

---

# ICANN

A centralized organization called ICANN maintains domain-related information.

Ideally, the flow would be:

1. User requests a website
2. Request goes to ICANN
3. ICANN provides the IP address
4. User reaches the correct server

---

# Problem: Single Point of Failure

If every request directly went to ICANN:
- ICANN would become overloaded,
- entire internet traffic would depend on it.

This creates a:
# Single Point of Failure (SPOF)

If ICANN goes down:
- many internet services could fail,
- companies could lose millions of dollars.

---

# Role of DNS Servers

Instead of all requests going to ICANN:
- requests are redirected to DNS servers.

DNS servers store cached copies of mappings.

This distributes the load and avoids ICANN becoming overloaded.

---

# Important Concept

ICANN can potentially become a single point of failure.

But DNS itself is designed in a distributed way, so:
- DNS does not rely on only one server,
- multiple DNS servers exist globally,
- data is replicated across them.

This helps improve:
- availability,
- reliability,
- scalability.






# Lecture2
case of delicious and it is a website hosted on a personal computer and it started getting traffic suddenly
the scale is 1 million save request and server can store 40 gb with other things like os , videos audio files other sioftwares 
we can increse the server to 300 gb but that is not the solution  we have just 5-0 days befire it runs out of space 
so we coyld have got a larger server but that is still not a permament solutiuon also cost will increase exponentially
here this example is vertical scaling 
now we r going to see horizontal scaling which is distributing our data across multiple servers where all of them may have same capacity this provides infinite storage 
when we have multiple servers shoudl we register all ofi these servers against the dns , can we have one isngle url and can we have mutiple url for the same ip address 
when we type the url of google we can get multiple ip adress 
from one url there are mutiple ip address
in ican can we have a url and then multiple ip sddress
the client request the dns servers  for the ip addressso at first the client just hits the ans serverand then the ip address is returned and then the client will
reach out to the server wuth teh same url request 
next time the dns might pick a different ip adress so client will recah ouyt to the diff server
the dat aof the user will be saved in one particular server so we cant go to another server next time , so this apprioach wont work it works for google 

WE need another server whose only job is redirecting and this is the node balancer , this maintains approximately same load , 
dns is going to give the ip address of the load balancer 
<img width="310" height="223" alt="image" src="https://github.com/user-attachments/assets/08bdcf30-cf09-4af5-a806-dc39c6324c01" />
user will only interact with the load balancer 
load balancer will redirect only to one server 
how exactly this mapp[ing is created , the load across all the server should be equal , 
we can use hashmap 
<img width="353" height="73" alt="image" src="https://github.com/user-attachments/assets/e44d54da-2736-4e4b-bf98-8855e27647c6" />
map will be user id with server , lets replace the servers with 0 , 1 , 2, 3 ,4 in reality it will  be ip address only so when user is requesting it will check the hasmap if its present then return that server or else just map to a random server 
<img width="309" height="270" alt="image" src="https://github.com/user-attachments/assets/5ee5df06-bc74-45e3-b47d-2d43852258f3" />
<img width="394" height="45" alt="image" src="https://github.com/user-attachments/assets/bf05828f-d3be-4d1d-843b-f329bb1ebf5a" />
no matter what data structure we use all those will be redirected through load balancer 
how do we ensure that our system does not crashes when the load balancer crashes 
instead of having a single load balanc er lets have a group of them but then we need a load balancer of a load balancer 
<img width="343" height="228" alt="image" src="https://github.com/user-attachments/assets/3d3f1a69-6265-427a-9e32-faa77e1c501c" />

so we didnt solvethe prblm we still have one single point of failure 
when a user sends request that first lb checks which lb is free then that lb redirects the user to the originzl server
<img width="306" height="200" alt="image" src="https://github.com/user-attachments/assets/93f914ee-5a8b-47ed-b2c1-2c21da3751a9" />
do we need the first lb , we dont need it , requests can randomly hit it 
if we can do this then we can register ip adress of all these load balancers against our  url 
since the request wil be redirected  randomly , so if the dns stores a list of ip addresses every time its going to show a random ip address when it returns so the load automatically gets  distributed randomly its not always going to pick pone ip address 
it will select those ip address which are nearer eto your location 
if i change my dns or network provider we will start seeing  a diff ip address 
now is there a prblm here 
diff load balancers will have diff mapping that rnadom server might not have the data of the server , the load balancers should share the data will all other load balancer 
what would be a better aproach 
we can maintain a hash function ->
before tis there are pther paproches as well
like what if we distribute the data accoridng to the geographical locations , we assign a particular server to a particular place 
<img width="351" height="150" alt="image" src="https://github.com/user-attachments/assets/110531be-29bb-4788-9969-6c6c381d3b14" />
so servers are dedicated place wise 
if we change the geographical location , ur server will chnage these lb cant remeber correctly where the data is stored basedon user id 
we can do a range based spltting 
first 300 gusers go to one server next bathc goes to another , this is a third approcach <img width="409" height="189" alt="image" src="https://github.com/user-attachments/assets/bf6a2fe2-ac6d-458e-9f0c-7df2ee7c1594" />
if there is any pattern in the distribution  then that pattern is going to  destroy this uniformity , uniformity can only be acheived if we have randomness  or if we have sudo randomness  but if we have a pattern we wont be getting uniform distribution thats is why even this approcah ownt work 
hash function 
what exactly is a hash function -> if i have a function f(x) which returns a square of x -> no
if i have a function f(x) which gives x%k -> this is a hash function 
y the first one is not a hash function while the seocnd one is 
wha t is the purpose of a hash function inside a hash map 
we get some dta athe data can be integer , string  , object , the data is  passed to a hash function  , that hash function returns  the index where the data should be stored  inside an array internally  , every array is going to have a seklf balancing binary tree 
we have strong this is oassed through a hash function  this func returns an index  somehow this function  is able to return a no which is  always a valid index and then whatwver valuwe this index has retuned 
what is the job of this function - to assign a function 
we take the user id and mod it with the no of servers we get  anumber between 0 to 3 
we redirect it to that serveer 
do we see any problem in this 
lets say there is a user with id 1 , 5 , 9 and so on  all of them will be redirected to server one but this can only happen if u dont have  any user with id 2  3 and  4  that wont happen irght  we will be generating the id sequentially since the ids are being generated sequentially  this is actually a round robin apporach so this is never going to happe n  
let us see what happens if another server comes <img width="345" height="258" alt="image" src="https://github.com/user-attachments/assets/5194be21-f156-4a0d-8e92-2c3e08671c14" />
now ist mod 5 
now a lot of users start getting 404 y bcoz now we have 5 servers  the user whose data was earlier stored in  server no 2 , so now when teh same user makes this request  this is not going to go to server 2 it is going to og to  server withh id 0 and this server is going to return 404 which means before u actually make this change the load balancer wil l have to go down  which means the entire system goes down for sometime but that will be a very small time bcoz these are  supposed to be very light weighted servers but before we do that we need to redistribute the entire data only then this 404 issue will not be there 
this seems like a good algorithem but its not 

Consistent hashing 
wer going to remove thi sdependency o  the count of servers we r going to have an independent hash function 
its going to take some input and return us some output depending on what hash function we r using for eg 0 to 10 raise to the power 18 
we will take the server id  and we will pass the value through the hash function <img width="379" height="166" alt="image" src="https://github.com/user-attachments/assets/c56bf560-a325-4454-ba06-ab6ff5063619" />
which is practically impossible 
<img width="427" height="169" alt="image" src="https://github.com/user-attachments/assets/41adb387-bebe-4249-bbd0-3560bc03b3e8" />

now we will keep this in an sorted array <img width="334" height="171" alt="image" src="https://github.com/user-attachments/assets/f72dc6a8-445f-411f-bf83-a68d4a8c233b" />
now what we will do is whenever  a request comes  we r going to pass the user id also  through the same hash function  on order to generate naother no in the range  from 9 to 10 raise to the power 18
whatver the next greater element is th eserver associated with that  is where this user should be stored 
<img width="278" height="219" alt="image" src="https://github.com/user-attachments/assets/daa65aeb-3bfa-4839-9601-d62c4ec332ae" />
how do i ensure that the distribution is uniform 
what happens when one of these servers goes down 
if a server goes down as per the algoeitrhme they will find the next greater elemnt , next greater is the next servereven that is going to go down so nit will go to next server this is cascadingf failure 
we need a way to prevenet cascading failure
if we adda new server , will it take load from all the server , we will take the server id and we r going to pass it through th hash function 
the load should be reudced uniformaly form all the servers but that is not happening here  
so instead od this aarnngement we get a slightlyd iff arangement   lets say we have a server which handles load of all the users geettuing hash in that particular range 
so we r fragmenting and giving a very smlal ragne to aprticualr server 
so basically we have one server only just that we r distributing its ranges this is gonna solve cascading failure <img width="340" height="250" alt="image" src="https://github.com/user-attachments/assets/b850cdbd-8ede-4da0-bd5b-e4edc6e2fd30" />
can we do this using hash function 
<img width="435" height="177" alt="image" src="https://github.com/user-attachments/assets/b90647f1-066f-406c-9bc1-dcd9e7df93b5" />
<img width="468" height="249" alt="image" src="https://github.com/user-attachments/assets/852ffa7d-a6ae-4086-9c32-eb4665ee253b" />

# Lecture 3 

the load balancer needs to know whoich server is up and which server is down these lb maintains a list of hashcode of all the servers , they r going to maintain a sorted list of hoshcode of servers which are currently  up  inorder to check whether the server is up or not there are 2 major ways , 
health check means the loab balancer is  going to send a pulse  , lb is going to pin all the servers individually inorder to chck whether they return a value or not , thi is supposed to be done by all the lb bciz theynneed to check their individusl network connection sas well , its possible that the network connection between the server and a load balancer is down that shouldbe taken as the server being down this is health check another way of doing this can be heartbeat which is a push based mechanisam the health one was pull based mechanism 
in the second way , load baalncer is not going to check whether the server is up or not server itself is going to inform the lb that im up and it is going to send the request to all the load balancer 
no of requests being transferred over the network will stah exactlt y the same 
which way do u think is better <img width="426" height="283" alt="image" src="https://github.com/user-attachments/assets/75286c4d-90d6-4fba-ac8d-b5c3667b060a" />
servers should be responsible for one isngle yhing , accept the request  give the respons server should not worry about how many lb are there whether a lb is there or not 
but int he second model the server needs to know how many lb are there and they need to maintain a lst of all the lb present whether a new is added or not
we r making abstarction here and breaking the single responsibility principle 
in the first eg lb should anyways have the data to all the servers 
hence in most of the cases healthcheck is more used 
but there are few examples where heart brest id used 
through thesemechanisams the lb get to know whether a server is up or down and the moment they get to know its down theyll be removing this server from this sorted list 
if this server is removed automatically will be redirected to the next server   
so its also possible that the next server also fails and if that happens then al of these request might be redirected to the next server this is cascading failure in order to solve this , instead of one single contagious range of a server me made ranges for each server 
so we have multiple small range , we r not increasing teh no of servers we r just distributing the range 
we have a ufnction h which gave us  1 position of a server when we have the same function again in another  value for the same server if u provide an input it is supposed to give the same output so one single func will not be sufficient  , we create multiple functions  , if we need 3 ranges then we need 3 different hash functions 
this was consistent hashing ans we did this bcoz we wnated to have a uniform distribution of loads  and we also wanted  the load balancers  to remeber were the data of a specific user is stored 
do u think there will be cases where even if the sysem doesnt know where the data is stored still the sustem is going to work perfectly fine can there be such cases 
what if the load balncer is completely uninformed , 
when u hit google.com the googles load balncer is going to redirect u  to speicifc application server , can the lb directly redirect the request using a round robin approach yes or na=o , it can , it should do this only and it should not apply any logic coz it will increse the time 
in real life we have load balancer then we have application servers then we have databse servers differently so there needs to be one load balancer sitting in front of the database servers  which needs to know which users data is stored in whioch serrvers  but the moment we doi this partitioning and segregate application server form database servers , now the application server hold no data now they are stateless nay users request can be redirected to any of these servers , but the behavior will be exactly the same bcoz they do not contain any data , they will forward the databse queries towards the load balancers and this db lb will decide whose request will be directed to which db server
now we can scale this seperately 
if we have very large data but we need very less computation we willl need multiple application servers , when we r expectinga  large volume of api hits
we r going to scale the db part when there is a lot of data to be staored 
the moment we implement consistent hashing here we add a factor of log n in my time 
but if theres no need to remeber whose data is stored where this prblm doesnt exist  so instead of using binary search inside that logic which adds a factor of log n in ur time complexity we can use a order 1 approach and we can reduce the time that the load bakalncer takes ot redirect , the round robin approach will be much more faster 
thsi will reduce the latency (time it takes for the request to  travel )<img width="445" height="262" alt="image" src="https://github.com/user-attachments/assets/e946af67-87e2-40d2-88ef-059ec36d024a" />
if latency reduces teh round trip time is also going to reduce 
if u remove consistent hasing and implement a singular algorithm , the time also reduces but we cant do the same thing in the database servers they need to be stateful bcoz they r holding data 
the lb in database servers needs to have consistent hashing 
so when ur using some software lets say 
if we dont cache things here in lb we will be following srp many network hops , increase the latency , 
reverse proxy ->haproxy , enginex lb + caching facility 

can we add a layer of cacing between the applixcayon servers and thae databse servers 
services like redis , aerospike thesea re nothign but key value pair storages which maintain the data in memory and they provide many functjionality but the most popularly used functionality is very similar ot that of a hashmap <img width="657" height="382" alt="image" src="https://github.com/user-attachments/assets/6674957b-6b02-4cd9-b5fe-65c3a18d3106" />
there is another cachign which is inherently present in any dtabse servers , in ur dbms servers , whenever u run a query in mysql or postgeres  ebfore executing it there are a bnch of stes thatthe databse management system follow in order to reduce the time that it takes to fetch the data , the query will be passed and then optimized internally  u might have joined two columns which are not indexed or if it possible to use the indexing  the databse systems are inteliigent enough to chnage ur query internally 
u might have used a subquery but the samequery might be more optimal if u use a join , the data wont just be returned , there is a cache inside db servers 
called as buffer pool 
we can have one redis server <img width="279" height="123" alt="image" src="https://github.com/user-attachments/assets/b8923295-d444-4413-bc33-253935b7afde" />
allll the requests will check cache first if its nt present then it will go to the db servers 
no we will distribute the ccache 
<img width="297" height="107" alt="image" src="https://github.com/user-attachments/assets/c7d76c7d-12ae-4604-9e6c-9e6cf1b24e93" />
and this distributed cache has a node balancer of its own 
<img width="488" height="310" alt="image" src="https://github.com/user-attachments/assets/6b51321b-518a-49d3-85be-f3bf4b778010" />
global caching means it is not specific t oa paplicatio  s4rver 
however we also have local cache 
cqching for speciifc application servers 
local cache is present in al of the application server and it happens in the case s hwen they r stateful bco in that case the data we r caching will be diff from each pther 
if every application server is specific to a patrticukar set of users in that case this cache canbe very specific to those users or those pridycut and then this cache can be maintained 
this cache can be spcific , either we can have a redis or aerospice server which is only in connection with one server 
or we can use this server itself to serve this from its own ram or form its own hard disk as well 
a hard disk which is a very slow stprage unit when it comes to cpu reading instructions that hard disk is fast enough to  make a mnetwork call
we can leverge the space which is already present in theses servers as a local cache 
<img width="351" height="300" alt="image" src="https://github.com/user-attachments/assets/a2aa0772-a17a-477f-ba9c-68268ec213f8" />
the green hoighlighted area is there local cache 

what is global cache and what is local cache  what is single cache nad what is distributed cache 
local cache is ingherently distributed , we cannot have a single sevrer maintaining local cache 
local cache can only be distribute 

challenges of caching 
1) space is  a problem  -> faster the storage smaller is goign to be the capacity , cdn will cost you a lot of money , cache will keep going full  so whenever u have a new request we make space by deleting in cdn there is expiry date , we need ot run a script to check their expiry date and validates them that is itself is going to be a heavy computation operation that will keep  their servers busy , hence we will use eviction , there are various different ytpe s of eviction algorithms one is least recently used
 <img width="517" height="117" alt="image" src="https://github.com/user-attachments/assets/6efe2d37-5835-49a8-8aa9-d3064bc0f3a0" />

2) another thing we know is that cachign is just storing the refernce of the opriginal data ,if the value is changed in the real servers it wnont update here , even if ur storing stale data it is not a prblm , suppose we both are wathcing reels and u get 3k views and i see 5k views but this differnece wont matter but what if it happens on a e commerece platform but when ur making a payement they should show the acyual prices, in cases where stale data is not working we have to ensure that the databse servers and the cache are always consistent -> cache invalidation


# Lecture 4 
in the last class we saw how to reduce latency by using caching , whih are of 2 types 
caching on client side and server side 
clicnt side means -> the data the files the media which we want to send to the client , which we send to the browser can be stored in 2 different places , in the browser itself  in the machine itself , the browser provides cookie , session storage , local storage and provied u a nosql database as well storing larger item , if u go to browser and u delete hisrtory  it will show how much data is being deleted there all those will be stord int he databse called indexed db all of these are present on the clients side 
there is another way of caching static data on the clients side  that is  cdn and we also saw that 70 percent  of the entire , if cdn is not there internet will be very slow
cdn does 2 things -> we have a client and it is accesingthe website through the browser or some application 
in my browser im opening amazon.com there should be only one request but there are more requests it can be links to slme css files , links to some js files 
if we remove cdn then all of these files will also go through this afrchitecture xome of these could be links to the s3 buckets , ethe entire data cannogt be stored in sql , we do not want redundancy here or any large files here so if u want ot have large files stored so we will use something smiilar to s3 servers 
problem -> a lot of time will be wasted , second it is also increasing the load on ur servers many applications are hitting ur application servers while many are hitting s3 servers , if we r using cdn we r solving this prbkm , 

on the server side there are 2 ways to implement caching , we have load balancers where we can cache the responses of some of the frequent api and if u have load balancers int he request directly then they will be called liversproxes 
majority of the times ur goign to cache ythe data between the application and the database servers  <img width="556" height="315" alt="image" src="https://github.com/user-attachments/assets/9ef33655-74eb-47c3-bc80-d00c8cc86b29" />
this is the g;lobal cache this also has 2 varieties , one single server or distributed one 
<img width="592" height="249" alt="image" src="https://github.com/user-attachments/assets/5f2b8788-3482-4ffd-afcf-4761ff367f6b" />
local cache means the cache will be insid ethe applicaytion server itself  
Which cache will have lower latency?
Local Cache
bcoz there is no network hop invoilved here 
to solev limited storage we need to have eviction locicy one of them is least recent or lru , another is lfu , least fruwnrtly used , first in first out , lifo , mru , mfu 
wht paramters will u decide 
we just use lru <img width="503" height="219" alt="image" src="https://github.com/user-attachments/assets/1389e04e-7e29-4fb2-a057-6a6beba16baa" />

cache may serve stale data -> whether we need consistency in our systen or not 
<img width="539" height="306" alt="image" src="https://github.com/user-attachments/assets/9dd27aac-8a6d-4683-a4dd-e77323f3ec50" />
hcing consistency is veryimp but is it a feature that is required mandatorly , can we lllive without consistency as well but data should be consistent but if ntg breaks thenm we can serve stale data 
in some times  we can serve this data but after fixed time this value should get updated , this cache should cachivee consistency with respe tc to your databse , there are 3 diff levels of consistency , immediate consistency , the miomengt there is a break in the data , it should dstart refracting in your cache , eventual consistency means that after sometime if it updated , that is ok for us and hving inconsistent data  which means there is no  guarantee , that it will get updated  but we r going to be ok with it ,
in financial matters it should get immadiate response also ticket booking 
leaderboard is goign to provide eventual consistency 
now eg of inconsisten data -> live streaming of a match , possible that the actual amount of viewers are different '
cache invalidation -> we need to check if the data we hve is valid or not 
ttl policy - a cache is ntg but a very large scale hasmap which has key valye pair 
THE key is a string and the value is an object 
along with data object we will also have a ttl associated with it , so etimes ttl is also a duration
<img width="590" height="183" alt="image" src="https://github.com/user-attachments/assets/99234192-6234-494a-a37a-b50ea1894ee6" />
the lkesser the ettl the more fresh the data 
<img width="465" height="150" alt="image" src="https://github.com/user-attachments/assets/dbcc22e6-fbc1-49c1-bab6-edc3df2a4621" />
we will do iteraion and delte all old entries but is this required coz for this we already have eviction policy 
hereinterviewers might confuse us 
ttl will provide us eventual consistency 
application servers creates queries which runs inside sql servers 
for knowing the table structure , we have classes implemented inside the code which are mapped to the entities in the databse , application servers know everything but cache is a dumb server
it is neither writing or executing sql quesries , cache doeanst imolemengt anythign cioz it doesnt habve business logic 
there r two diff problems and 2 diff solution
<img width="602" height="246" alt="image" src="https://github.com/user-attachments/assets/eb568c65-8be4-4565-8eab-09b56049d20d" />
applicastion server is saying in the databse servers hence it should also updat ein the cace 
first the db returns success tehn it will try t o write in the cace then the app servers will return success to 
if one fauils teh entire transaction fails 
we have one single serverwhere we have installed our database management system , this server has one single operating system , it is able to leverage the functionalities provided by the os , they have sared ram , they have  shared loss so inside one singl eserver, it is very easy to implement transacitons 
when it comes to distributed servers maintaining stomicity is on e of the hardest prblm to solve 
so if u have this type of caching mechanisam which increases the latency when it comes to write  , this is known as write through cache <img width="620" height="246" alt="image" src="https://github.com/user-attachments/assets/83c7abf3-d030-412e-a563-4bf648aa366c" />
this provides immediate consistency
ok so we have 2 mechanisms , in one we have ttl where we read the data then we check if we  have expiry date , if the expiry date is passed then we delete the data another is write through cache where we need 2 faced we write and wait for the success response ,then we write in the cache and we wiat for the success response ,  this increases the latency 
let us have a use case now 
what if we have to lets say ,cricket match goin on and we have to display the win percentage of the two teams which caching mechanism out of these 2 should be used , should we use ttl or write through , are we ok with eventual consistency or do we need immediate consistency 
are all of u aware what is win percentage ,after toss the percentage might change 
as the game progresses win percentage changes this should also be stored in some kind of cache , this cache should it be detailed base or should it be write through cache , r we ok with eventual consistency  or do we need immediate consistency 
if we get immediate consistency  will we be ok with it 
so we need 01 secs to calculate but in this time the next ball is done so mimmediate consistency in this case is impossible bcoz the speed of the game is faster so in that case we will go ahed wit ttl 
lets see what eill happen if we implement ttl in tis case 
there is no data in the cacahe 
application server makes one request , app servers checks the cacahe that there is no data app servers goes to the databse , the databse returns the entire data that is needed inorder to do the ca;lculation , which means that we r running very complicated queries over here,and this sefrver is going to do a lot of processing in order to manipulate the data inorder to calculate these numbers and then it is going to wfrite in this acche with this a ttl is also going to be there , so ttl lets say it is set ot be 15 or 20 mins in this time we willd o the entire calculation 
let us see what really is going to happen after 20 mins when this ttl expires there is a request from a user the request goes to lets say the first serverthe server checks the cacheand it gets the data but the ttl is expired which means that server has to do the entire calculation again at the same time other servers may also requestthis server also checks the cache this s4rver also sees that this is a acahe so this server is also going to do the complete heavy computation 
so there are millions of users and the servers will be busy so we souldnt be doing that , the calculkation should be done once and it hsould be available toa ll theservers but if we have ttl 
one server cant talk to another and say that im doing this computation thats not goign to happen all of these reach out to databse doing these complicated queries 
so ttl althought it provides us consistency  is not the right invalidation policy in this case 
in fact what we should be doing if u were probably not aware of ttl u would have come up witha better solution for this , which will be that we run a chrome job , we have a script we will run that script lets say after every 20 mins that script os going to fetch teh data and that script will ensure that the data gets stored in teh cache ,application serverds are not gojng to store data inside the cache , the script runs parallel to the servers every 20 mins and rewrites 
ttl can result in these of issues with heavy ciputtaion 
ewhich may take down our entire databse servers
so its better we run a job in parallel , chrone job is just a script which runs after every we can just schedule that script 
for the application servers thehy will always reach opout to the acche if the data i sthere we will serve but if the data is not there we will not serve winning percentage at all but the data will always be here , we will always first compute the data then update it , this way of validating the cache is called as write aroubnd 
this is not happening inside the system , 
this is anotehr invalidation policy and we will use it only when there is very heavy computation neened 
now let us go the in stagram view count or live
inside the instagram databse , there will be multiple tables
what happens 2when a reel got viraland iti s getting millions of views suddenly there is a spike ina  no of viewd then what is appening in the dtabse level 
every reel is a row <img width="385" height="141" alt="image" src="https://github.com/user-attachments/assets/ddc1d851-8571-4b3a-aac4-be31e7b0b24a" />
the moment a new view and like comes the data should change 
but the row will be locked hence the reel wont show , instead of directly writing the databse 
can we write the data in the cache first 
as of now any write query it was going directlyt to the databse with the assumption that thed atabse is the single source of truth 
ram as temporary data , the data form ram will be avicted the data form ram will be invalidated if the power goes down since cache is going to maintain the data in the ram the data will be completely washed away tahts y we havethis persisetnt data storage but in this case can we write the data in the ram instaed of the sql servers , should we do write opearations on theram 
so as per the correct architecture what will happen is that 
the request comes to lb then to application servers if it is a view opeartyooon or a like api , coz whenever we like then an api is called some table inside some databse cna be changed this is what is happening right now but if there are 10s and thosands of users watching againa nd agin oresisngthe like button again ane dgain this will make the dtabase go down 
so can weionce we have some x no of writes instaed fo writing here , write this insicde the cache what wecan do is once we have some x no of writes already done time to time we can run a script similar to this one but this time we r making a databse with the cache , the most updated data is now going to be present inside the cache 
we can clonejobin paralle and tis will also be goign to update the databse 
do u think there are any issues tehr ein this design 
cache may not go down bcoz of the load but it may go down for nay other reason
if cache goes down data goes down 
<img width="523" height="215" alt="image" src="https://github.com/user-attachments/assets/f779efc3-c5ad-4d40-a6d4-1d44706aa99a" />
cache has 11k and then the databse gets 11k but then cache gts updates to 11.2k but then the cache goes down and the data is lost permanently should we be ok with this
in some cases we r ok with using data as well , we might have experienced that we have liked a reel when we see that samereel form different aaccount thta liek isnt there so we relike 
so this cache is goign to be infrequent
we need to lose as less data as possible
but sometimes it comes to views in reels and even likes it is ok for us to lose the data , if it is 1.234 million views or even 1.256 millions it doenst matter coz user will see only 1.1. million vioews 
hence this way of writing will also work 
we can write in the cache and then we can write in the databse afterwards so this way of acche invalidation is known as write back cache 
what should be the frequency wiuth which we should be reaching out to the databse inorder ot do this , is compleetly dependent on my mine frequency can be few seconds , minutes and months 
but this can only be oimplememnted in cases where we r ok losing some if teh data 
slo we have seen 4 ways of cache invalidation , these are not the ways of cache eviction 
that is different  it solbes the prblm of limited storage 
in all these 4 ways we have been solving consistency 
we need to decide whether we want immediate , eventual, inconsistent data 
this was all we need to knew about caching 
lets take a problem statement 
this was oslved in scaler when it was interviewbit , its sim ilar to leetcode , 
in inyterview bit we open a prblem we see the prblma nd code editor , , internally my request uis forst going to got set of  load baalncer , many application servers ,whenever ur trying to solve a prblm there will be a request that is goign to go this request should have ur code as well , bcoz the code wont be executed on the clients side , it will be executed on server side , so ur entire code goes as a part of the requets then the load balancer is goign to redirect it to one of the application servers , depeneding on whether the servers are statless or statefull , if they are statefull ur request is always goign to go through one particular server if they are stateless then they may go to any of the server 
so once this request goes here the application server does some validation , they check if teh user is authorized , or the langige is svoorect or not , what is the time and meory limit 
for that first they need to flag some dayat , they r going to fetch thuis data formthe databse servers , in scaler we use amazon rds ,relational database servers 
for storing the data in sql dayase , all the rds servers are goignt o provide us postgre which is a sql databse 

app severe willr each out to dfatabse servers they will take all the info of the prblm that we r going to osve so there is goign to be a problem id which is part of the request and it fetches the entireitet cases are goignt o be stored in files formation about the problem which will include time limit , memory limit , the languages in which we can write the code then it does some validation here and now it has to execute this code executing teh code requeres test cases tehre will be some small test cases and some large tets cases there will be some test cases for testing the memory so there r multiple files of test cases , where should be store the files sould we store the file in the same sql databases , so where should we store the file ,we sould store the file in a seperate storage server (s3) amaxozn provides this simple storage servers where we can store very large fiels other cloud servers provide us other diff types of file storage systems , we do not want normalized data when it comes to files we simply want to store them as blocks , the test cases are stoed as files inside  the s3 servers 
inside the data we have the exact location of the testcase we have the url, we fetch teh url from out sql data and then these servers will reach out to s3 and then these s3 servers are going to return the test cases os these test cases will now be downloaded this downloading ius something which incrases the latency a lot bcoz these test cases are not small files , it can be 700mb to 1 gb of 1 file , downloading mutiple fielsis goignt o increase the latenycy 
the user who has solved this problem is waiting for these files to get downloaded, which means that the latency is too much , bcoz fater the donwloading the code should also execuite wich is already compuytationally heavy 
so how do we reduce teh latency here 
so where hsould  be implemt the cache what shodl be the e iction policy , validation policy ,do we need a global or local cace , do we need a distributed cache or a single server cache , these are all the answers that we have to find out 


## High-Level Architecture Requirements
- **Target DAU:** 10 Million Active Users
- **Read/Write Ratio:** 100:1 (Read Heavy Architecture)
- **Availability SLA:** 99.99% Availability (~52.6 min downtime/yr)
- **Latency Budget:** P99 Latency < 100ms for core read APIs.

## High-Level Architecture Requirements
- **Target DAU:** 10 Million Active Users
- **Read/Write Ratio:** 100:1 (Read Heavy Architecture)
- **Availability SLA:** 99.99% Availability (~52.6 min downtime/yr)
- **Latency Budget:** P99 Latency < 100ms for core read APIs.
