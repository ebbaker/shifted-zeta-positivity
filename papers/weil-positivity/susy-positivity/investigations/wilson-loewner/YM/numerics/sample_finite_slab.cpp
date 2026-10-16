// Finite open-time SU(2) Wilson slab. Prepared for Edward Baker, 2026-09-24.
// GPT-6 (Codex) assisted; reasoning effort not exposed, not inferred.
// U = q0 I - i q.sigma, so quaternion multiplication uses +cross.
#include <array>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <vector>
using namespace std;
struct Q {
 double a=0,x=0,y=0,z=0;
 Q operator+(Q b)const{return {a+b.a,x+b.x,y+b.y,z+b.z};}
 Q operator-(Q b)const{return {a-b.a,x-b.x,y-b.y,z-b.z};}
 Q operator*(double s)const{return {a*s,x*s,y*s,z*s};}
 Q operator*(Q b)const{return {a*b.a-x*b.x-y*b.y-z*b.z,
 a*b.x+x*b.a+y*b.z-z*b.y,a*b.y+y*b.a+z*b.x-x*b.z,
 a*b.z+z*b.a+x*b.y-y*b.x};}
 Q adj()const{return {a,-x,-y,-z};}
 double dot(Q b)const{return a*b.a+x*b.x+y*b.y+z*b.z;}
};
const Q one{1,0,0,0};
using Word=vector<int>; // signed directions +/-1..4; 4 is physical time
struct Slab {
 int L,nt,V; double beta; vector<Q> u; vector<array<int,4>> up,dn,coord;
 mt19937_64 rng; uniform_real_distribution<double> unif{0,1};
 normal_distribution<double> normal{0,1}; long long accepted=0,proposed=0;
 Slab(int l,int n,double b,unsigned long long seed,bool hot):L(l),nt(n),V(l*l*l*n),beta(b),u(4*V),up(V),dn(V),coord(V),rng(seed){
  for(int s=0;s<V;s++){
   int z=s; for(int d=0;d<4;d++){int len=d==3?nt:L;coord[s][d]=z%len;z/=len;}
   for(int d=0;d<4;d++){
    auto c=coord[s]; int len=d==3?nt:L;
    c[d]=(c[d]+1)%len;up[s][d]=(d==3&&coord[s][d]==nt-1)?-1:index(c);
    c=coord[s];c[d]=(c[d]+len-1)%len;dn[s][d]=(d==3&&coord[s][d]==0)?-1:index(c);
   }
  }
  for(int s=0;s<V;s++)for(int d=0;d<4;d++)u[4*s+d]=hot?haar():one;
 }
 int index(array<int,4> c)const{return c[0]+L*(c[1]+L*(c[2]+L*c[3]));}
 Q haar(){Q q{normal(rng),normal(rng),normal(rng),normal(rng)};return q*(1/sqrt(q.dot(q)));}
 Q plaquette(int s,int d,int e)const{
  return u[4*s+d]*u[4*up[s][d]+e]*u[4*up[s][e]+d].adj()*u[4*s+e].adj();
 }
 Q staple(int s,int d)const{
  Q h{};int sd=up[s][d];
  for(int e=0;e<4;e++)if(e!=d){
   int se=up[s][e];
   if(se>=0&&up[sd][e]>=0)h=h+u[4*sd+e]*u[4*se+d].adj()*u[4*s+e].adj();
   int sm=dn[s][e];
   if(sm>=0&&up[sm][d]>=0){int smd=up[sm][d];h=h+u[4*smd+e].adj()*u[4*sm+d].adj()*u[4*sm+e];}
  }return h;
 }
 // Action includes constant 1 per plaquette; sectors -1,0,+1 relative to site reflection.
 array<double,3> action_parts()const{
  array<double,3> out{};int mid=nt/2;
  for(int s=0;s<V;s++)for(int d=0;d<4;d++)for(int e=d+1;e<4;e++)if(up[s][d]>=0&&up[s][e]>=0){
   int t=coord[s][3]; int sector=e==3?(t<mid?0:2):(t<mid?0:(t==mid?1:2));
   out[sector]+=beta*(1-plaquette(s,d,e).a);
  }return out;
 }
 double action()const{auto x=action_parts();return x[0]+x[1]+x[2];}
 double plaq_mean()const{
  double v=0;int n=0;for(int s=0;s<V;s++)for(int d=0;d<4;d++)for(int e=d+1;e<4;e++)if(up[s][d]>=0&&up[s][e]>=0){v+=plaquette(s,d,e).a;n++;}return v/n;
 }
 void sweep(double delta,int hits){
  for(int s=0;s<V;s++)for(int d=0;d<4;d++)if(up[s][d]>=0){
   Q h=staple(s,d);Q v=u[4*s+d];
   for(int k=0;k<hits;k++){
    double theta=delta*(2*unif(rng)-1);int axis=int(3*unif(rng));
    Q r{cos(theta),0,0,0};if(axis==0)r.x=sin(theta);if(axis==1)r.y=sin(theta);if(axis==2)r.z=sin(theta);
    Q w=r*v;double diff=beta*((w*h).a-(v*h).a);proposed++;
    if(diff>=0||log(unif(rng))<diff){v=w;accepted++;}
   }u[4*s+d]=v*(1/sqrt(v.dot(v)));
  }
 }
 Q walk(int &s,const Word &p)const{
  Q q=one;for(int a:p){int d=abs(a)-1;if(a>0){if(up[s][d]<0)throw runtime_error("path leaves slab");q=q*u[4*s+d];s=up[s][d];}else{if(dn[s][d]<0)throw runtime_error("path leaves slab");s=dn[s][d];q=q*u[4*s+d].adj();}}return q;
 }
 pair<Q,Q> loop_probe(int anchor,const Word &trace,const Word &chord)const{
  int s=anchor;Q t=walk(s,trace);int end=s;s=anchor;Q c=one,b{};
  int m=chord.size();
  if(m==0){Q p=plaquette(s,0,1);b={0,p.x/2,p.y/2,p.z/2};}
  else for(int j=0;j<=m;j++){
   Q p=plaquette(s,0,1);p.a=0;
   double weight=(j==0||j==m?.5:1.)*j/(double(m)*m);
   b=b+(c*p*c.adj())*weight;
   if(j<m){Word edge{chord[j]};c=c*walk(s,edge);}
  }
  if(s!=end)throw runtime_error("trace/chord endpoints disagree");
  return {t*c.adj(),b};
 }
 vector<double> measure(const vector<Word>&trace,const vector<Word>&chord)const{
  int n=trace.size();vector<double> out(1+n*n+n*9+(n-1)*9,0);out[0]=plaq_mean();
  for(int s=0;s<V;s++)if(coord[s][3]==nt/2){
   vector<Q> q(n);vector<array<Q,3>> b(n);
   for(int i=0;i<n;i++){auto p=loop_probe(s,trace[i],chord[i]);q[i]=p.first;b[i]={one,p.second,one*p.second.dot(p.second)};}
   int off=1;
   for(int i=0;i<n;i++)for(int j=0;j<n;j++)out[off++]+=q[i].dot(q[j])/(L*L*L);
   for(int i=0;i<n;i++)for(int j=0;j<3;j++)for(int k=0;k<3;k++)out[off++]+=b[i][j].dot(b[i][k])/(L*L*L);
   for(int i=0;i<n-1;i++){
    Q step=q[i+1]*q[i].adj();
    for(int j=0;j<3;j++)for(int k=0;k<3;k++)out[off++]+=b[i+1][j].dot(step*b[i][k])/(L*L*L);
   }
  }return out;
 }
};
void require(bool b,const char *s){if(!b)throw runtime_error(s);}
int main(int argc,char**argv){try{
 if(argc!=12){cerr<<"usage: sampler L Nt beta seed hot burn sweeps thin delta hits paths.txt\n";return 2;}
 int L=stoi(argv[1]),nt=stoi(argv[2]);double beta=stod(argv[3]);
 require(L>=3&&nt>=3&&nt%2==1,"need L>=3 and odd Nt>=3");
 unsigned long long seed=stoull(argv[4]);bool hot=stoi(argv[5]);int burn=stoi(argv[6]),sweeps=stoi(argv[7]),thin=stoi(argv[8]);double delta=stod(argv[9]);int hits=stoi(argv[10]);
 ifstream in(argv[11]);int n=0;in>>n;require(n>=2,"missing paths");vector<Word> trace(n),chord(n);
 for(int i=0;i<n;i++)for(auto *w:{&trace[i],&chord[i]}){int m;in>>m;for(int j=0;j<m;j++){int d;in>>d;require(abs(d)>=1&&abs(d)<=3,"spatial paths only");w->push_back(d);}}require(bool(in),"bad path file");
 // Independent checks use a different RNG and do not change the measurement stream.
 Slab test(L,nt,beta,seed+1000000,true);double err=0;
 for(int j=0;j<40;j++){
  int s=(j*101)%test.V,d=j%4;if(test.up[s][d]<0)continue;
  Q old=test.u[4*s+d],w=test.haar(),h=test.staple(s,d);double before=test.action();test.u[4*s+d]=w;
  err=max(err,abs((test.action()-before)+beta*((w*h).a-(old*h).a)));test.u[4*s+d]=old;
 }require(err<1e-9,"staple/action mismatch");
 auto before=test.measure(trace,chord);double action=test.action();auto save=test.u;
 vector<Q> g(test.V);for(auto &q:g)q=test.haar();
 for(int s=0;s<test.V;s++)for(int d=0;d<4;d++)if(test.up[s][d]>=0)test.u[4*s+d]=g[s]*save[4*s+d]*g[test.up[s][d]].adj();
 auto after=test.measure(trace,chord);double gauge=abs(test.action()-action);for(size_t j=0;j<before.size();j++)gauge=max(gauge,abs(before[j]-after[j]));require(gauge<1e-9,"gauge covariance mismatch");
 test.u=save;auto parts=test.action_parts();
 for(int s=0;s<test.V;s++)for(int d=0;d<4;d++)if(test.up[s][d]>=0){auto c=test.coord[s];c[3]=nt-1-c[3]-(d==3?1:0);Q q=save[4*test.index(c)+d];test.u[4*s+d]=d==3?q.adj():q;}
 auto reflected=test.action_parts();double ref=0;for(int j=0;j<3;j++)ref=max(ref,abs(parts[j]-reflected[2-j]));require(ref<1e-9,"reflection action mismatch");
 test.u=save;double unit=0;for(auto q:save)unit=max(unit,abs((q*q.adj()).a-1));require(unit<1e-12,"unitarity mismatch");
 cerr<<setprecision(17)<<"{\"action_delta_error\":"<<err<<",\"gauge_error\":"<<gauge<<",\"reflection_error\":"<<ref<<",\"unitarity_error\":"<<unit<<"}\n";
 Slab model(L,nt,beta,seed,hot);for(int i=0;i<burn;i++)model.sweep(delta,hits);
 model.accepted=model.proposed=0;cout<<setprecision(17);
 for(int i=0;i<sweeps;i++){
  model.sweep(delta,hits);if((i+1)%thin==0){auto v=model.measure(trace,chord);for(size_t j=0;j<v.size();j++){if(j)cout<<' ';cout<<v[j];}cout<<'\n';}
 }
 cerr<<setprecision(17)<<"{\"acceptance\":"<<double(model.accepted)/model.proposed<<",\"measurements\":"<<sweeps/thin<<"}\n";
 return 0;
}catch(const exception&e){cerr<<e.what()<<'\n';return 1;}}
