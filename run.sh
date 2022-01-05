cd $(dirname $0)

gh repo clone thecodeisalreadydeployed/testdata workspace
cd workspace
ls

git switch testdata
echo -e "// $(date)\n\n$(cat nx/apps/nest-a/src/main.ts)" > nx/apps/nest-a/src/main.ts
cat nx/apps/nest-a/src/main.ts
