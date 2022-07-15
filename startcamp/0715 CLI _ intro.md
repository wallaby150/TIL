# CLI _ INTRO

> CLI란 command-line interface, 명령 줄 인터페이스.
>
> **- Why CLI**
>
> - GUI는 CLI에 비해 사용하기 쉽지만, 단계가 많고 컴퓨터의 성능을 더 많이 소모.
> - CLI 환경이 좀 있다.

---

## 각종 명령어

### \- 파일 생성

 Git bash를 열고 하나씩 해봅시다!

- touch

```bash
$ touch {파일명}
```

\+ `{}`는 가변형이라는 뜻이다. _ 원하는 거 적어넣어라.



- ls

 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어.

```bash
$ ls
$ ls -a		# 좀 더 다양한 정보를 확인.
$ ls -l		# 언제 누가 만들었는지 확인 가능.

$ pwd		# 내 절대경로 보기 가능.
```

\+ `ctrl + l`은 화면 올리기.



- Mkdir

  새 폴더를 생성하는 명령어 (make directory를 의미.)

```bash
$ mkdir {my_folder}
```



- cd

  현재 작업 중인 디렉토리를 변경하는 명령어. (change directory를 의미.)

```bash
$ cd {my_folder}/
$ cd ..
$ cd {lectures}/{startcamp}/		#한 번에 이동 가능
$ cd ../../

$ cd le 					#파일/폴더가 하나면 여기까지만 치고 탭해도 바로 넘어가진다.
```

\+ `..`은 상위폴더를 의미한다.



- start/open

​		폴더/파일을 여는 명령어 (windows는 start, mac에서는 open을 사용)

- rm

```bash
$ rm {trash.md}				#확장자까지 쳐야 함.
$ rm -r {my_folder/}		#'recursive'라고 재귀. 거기 있는 거 다 지워라.
```



## 절대경로 vs 상대경로

- 절대경로
  - 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
  - 윈도우 바탕화면의 절대 경로 -C:/Users/ssafy/Desktop
- 상대경로
  - 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것.

../ 현재 작업하고 있는 폴더의 상위 폴더

./ 현재 작업하고 있는 폴더