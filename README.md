# Auto-IR-Analysis_Architecture_In_AWS

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
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
1. AWS 침해사고 증가
Capital one 사건은 AWS 클라우드 환경에서 발생한 침해사고로, 해커가 AWS EC2 인스턴스에 악의적인 요청을 보내어 임시 로그인 자격 증명을 획득 하였다.
최대 1억명의 Capital one의 고객 개인정보가 유출된 매우 심각한 사건임에도 발생시점과 발견 시점의 5개월 간의 간격이 존재하는 문제점이 발견되었다.
위 사례처럼 클라우드 침해 사고 발생 시 이를 분석하기 위한 자동화 구성은 중요하고, 해당 구성에 따라 관리자가 더 빠른 시일 내로 알아차려 사고를 수습하기 위한 골든타임을 놓치지 않을 수 있다

2. 많은 기업들이 클라우드 환경으로 마이그레이션
"배달의 민족"서비스를 운영하는 푸드테크 기업 "우아한 형제들"은 4년간의 준비 끝에 AWS라는 클라우드 서비스로 모든 서비스를 마이그레이션하였다.
이처럼 다양한 기업들이 기업 특성에 맞추어 온프레미스 환경에서 클라우드 환경으로 마이그레이션 하고 있는 것을 확인 할 수 있다.

3. On-premise / Cloud 환경 차이로 발생하는 어려움
온프레미스 환경의 경우 데이터에 대한 접근 및 제어가 가능하여 침해사고 대응이 상대적으로 용이하지만 클라우드 환경의 경우 물리적 자원에 대한 직접적인 접근이 제한적이며 보안 사고 발생 시 가시성과 통제성이 떨어진다.
또한 가상화 소프트웨어 내에 보안 취약점이 존재하며 Multi-tenancy 환경이므로 보안 취역점이 확산될 수 있는 위험이 있다.

4. 관련 법안
클라우드컴퓨팅 발전 및 이용자 보호에 관한 법률 제23조에 따르면 클라우드 컴퓨팅 서비스 제공자는 클라우드 컴퓨팅 품질 / 성능 및 정보보호 수준을 향상시키기 위하여 노력하여야 한다.


## 서버 인프라 구축
서버 VPC
1. VPC 설정
    * Server_VPC 생성
2. Subnet
    * Public Subnet
    * Private Subnet
3. Security Group
    * ~~
4. EC2 오토스케일링
    * 사용자가 지정한 규칙에 따라 EC2 인스턴스 수를 자동으로 조정하는 서비스
    * 오토스케일링 그룹을 통해 최소 두 개의 EC2가 오토스케일링 되도록 설정
    * Route53에 cumulus.kro.kr 도메인 레코드 할당??
5. ALB
    * ~~
6. NAT gateway
    * ~~
7. WAF 로깅
    * ~~
8. Endpoint 및 Gateway
    * ~~
9. GuardDuty
    * ~~

분석 VPC
1. VPC 설정
    * ~~
2. Endpoint 및 Gateway
    * ~~
3. EC2
    * ~~
4. Security Group
    * ~~


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
