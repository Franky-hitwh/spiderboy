#!/usr/bin/env python
#coding=utf8
"""
    ORM映射：关联数据库表
"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()


class GK_13_L(Base):

    __tablename__ = 'gk_13_l'
    
    id = Column(Integer,  primary_key=True, autoincrement=True)
    nf = Column(String(100))
    kl = Column(String(100))
    zy = Column(String(100))
    
    xx = Column(String(100))
    pc = Column(String(100))
    bzylqrs = Column(String(100))
    zgfxc = Column(Integer)
    zdfxc = Column(Integer)
    pjfxc = Column(Integer)
    zgf = Column(String(100))

    zdf = Column(String(100))
    pjf = Column(String(100))
    
    zgfmc = Column(String(100))

    zdfmc = Column(String(100))
    pjfmc = Column(String(100))


class GK_13_W(Base):

    __tablename__ = 'gk_13_w'
    
    id = Column(Integer,  primary_key=True, autoincrement=True)
    nf = Column(String(100))
    kl = Column(String(100))
    zy = Column(String(100))
    
    xx = Column(String(100))
    pc = Column(String(100))
    bzylqrs = Column(String(100))
    zgfxc = Column(Integer)
    zdfxc = Column(Integer)
    pjfxc = Column(Integer)
    zgf = Column(String(100))

    zdf = Column(String(100))
    pjf = Column(String(100))
    
    zgfmc = Column(String(100))

    zdfmc = Column(String(100))
    pjfmc = Column(String(100))


class YX_INFO(Base):

    __tablename__ = "yx_info"
    id = Column(Integer,  primary_key=True, autoincrement=True)
    yxmc = Column(String(100))
    yxcc = Column(String(100))
    yxpm = Column(String(100))
    
    szdq = Column(String(100))
    yxls = Column(String(100))
    bxlx = Column(String(100))




class ZY_INFO(Base):

    __tablename__ = "zy_info"
    id = Column(Integer,  primary_key=True, autoincrement=True)
    xkml = Column(String(100))
    zyl = Column(String(100))
    zydm = Column(String(100))
    
    zymc = Column(String(100))
    xkdm = Column(String(100))
    yjxk = Column(String(100))


class XK_INFO(Base):

    __tablename__ = "xk_info"
    id = Column(Integer,  primary_key=True, autoincrement=True)
    xkdm = Column(String(100))
    xkcc = Column(String(100))
    xkmc = Column(String(100))
    xx = Column(String(100))
    
    add = Column(String(100))
    yjxk = Column(String(100))
