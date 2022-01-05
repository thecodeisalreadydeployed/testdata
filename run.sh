cd $(dirname $0)

gh repo clone thecodeisalreadydeployed/testdata workspace
cd workspace
ls

git switch testdata
sed -i "1s;^;// $(date)\n\n" nx/apps/nest-a/src/main.ts
cat nx/apps/nest-a/src/main.ts
