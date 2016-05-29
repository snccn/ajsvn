# this is the table design of the project zjsvn
# here only store the sql commands and it will be used

CREATE_TABLE='''
create table IF NOT EXISTS moeship (
id int primary key,
name varchar(255),
star int ,
wedding text,
desc text,
level varchar(255),
nickname varchar(255),
getting text,
shecheng varchar(255),
pinyin varchar(255),
zidan int,
oil int,
life int,
lifemax int,
shanbi int,
shanbimax int,
defence int,
defencemax int,
no varchar(255),
oilcost varchar(255),
ironcost varchar(255),
zhencha int,
zhenchamax int,
nation varchar(255),
dazai int,
fenbu varchar(255),
speed varchar(255),
rocket int,
rocketmax int,
upgrade int,
upgradeinfo varchar(255),
isbuild int,
buildtime varchar(255),
weapon varchar(255),
img varchar(255),
img_bb varchar(255),
focus varchar(255)
);
'''
