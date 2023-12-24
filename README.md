# Auto-IR-Analysis_Architecture_In_AWS

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="Auto-IR-Analysis_Architecture_In_AWS/Image/아키텍쳐.png" width="1000" height="1000">
  </a>

  <h3 align="center">AWS 환경에서 침해사고분석을 위한 자동화 아키텍쳐 구성</h3>

  <p align="center">
    본 프로젝트는 화이트햇 스쿨 1기 뭐시깽이에서 진행된 프로젝트입니다.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>

## Index

- [프로젝트 개요](#프로젝트-개요)
  - [팀원 소개](#팀원-소개)
  - [프로젝트 필요성](#프로젝트-필요성)
      
- [서버 인프라 구축](#서버-인프라-구축)
    
- [Contributing](#contributing)
    
- [Authors](#authors)
- [License](#license)

## 프로젝트 개요

### 팀원 소개

### 프로젝트 필요성

## 서버 인프라 구축

## 아티팩트 채증 자동화

## 아티팩트 분석 자동화

취약 자바 설치 :

```sh
curl -L -b "oraclelicense=accept-securebackup-cookie" -O https://download.oracle.com/otn/java/jdk/8u20-b26/jdk-8u20-linux-x64.tar.gz

tar -zxvf jdk-8u20-linux-x64.tar.gz

cd jdk1.8.0_20

export JAVA_HOME=$(pwd)

export PATH=$PATH:$JAVA_HOME/bin

echo 'export JAVA_HOME=$(pwd)' >> ~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> ~/.bashrc
source ~/.bashrc

java -version
```

톰캣설치:

```sh
wget http://archive.apache.org/dist/tomcat/tomcat-8/v8.0.36/bin/apache-tomcat-8.0.36.tar.gz

tar -xzvf apache-tomcat-8.0.36.tar.gz

cd apache-tomcat-8.0.36

앱 뭐시꺵이에 ROOT로 이름 바꿔서 war넣고 

cd bin

./catalina.sh run
```

## 표 + 사진 방법 1

| JavaScript | TypeScript |  React   |  Node   |
| :--------: | :--------: | :------: | :-----: |
|   ![js] 사진들어갈곳   |   ![ts]    | ![react] | ![node] |

## 표 + 사진 방법 2

| <img src="이미지경로" alt="이름" width="16px" height="16px" /> 이름 | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 11+ | Yes | Yes | Yes |


##
[js]: /git 내 이미지 경로
[ts]: /git 내 이미지 경로
[react]: /git 내 이미지 경로
[node]: /git 내 이미지 경로
