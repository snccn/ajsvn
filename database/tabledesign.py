# this is the table design of the project zjsvn
# here only store the sql commands and it will be used

CREATE_TABLE='''
create table IF NOT EXISTS moeship (
id int primary key,
name varchar(255),
star varchar(255) ,
wedding text,
desc text,
level varchar(255),
nickname varchar(255),
getting text,
shecheng varchar(255),
pinyin varchar(255),
zidan varchar(255),
oil varchar(255),
life varchar(255),
lifemax varchar(255),
shanbi varchar(255),
shanbimax varchar(255),
defence varchar(255),
defencemax varchar(255),
no varchar(255),
oilcost varchar(255),
ironcost varchar(255),
zhencha varchar(255),
zhenchamax varchar(255),
nation varchar(255),
dazai varchar(255),
fenbu varchar(255),
speed varchar(255),
rocket varchar(255),
rocketmax varchar(255),
upgrade id,
upgradeinfo varchar(255),
isbuild varchar(255),
buildtime varchar(255),
weapon varchar(255),
img varchar(255),
img_bb varchar(255),
focus varchar(255)
);
'''
