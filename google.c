#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main()
{
FILE *fp;
char *buf;
int cnt;
system("nmcli device status>state.txt");
fp=fopen("state.txt","r");
fseek(fp,0,2);
cnt=ftell(fp);
fseek(fp,0,0);
buf=calloc(1,cnt);
fread(buf,cnt,1,fp);
printf("%s",buf);
fclose(fp);
if(strstr(buf,"connected"))
{
system("firefox -new-tab http://www.google.com");
}
else
{
printf("not connected");
}
}
