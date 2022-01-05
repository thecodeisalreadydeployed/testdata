cd $(dirname $0)

gh repo clone thecodeisalreadydeployed/testdata workspace
cd workspace
ls

git switch testdata
echo "// $(date --iso-8601=seconds)\n\n$(cat nx/apps/nest-a/src/main.ts)" > nx/apps/nest-a/src/main.ts
cat nx/apps/nest-a/src/main.ts

git add nx/apps/nest-a/src/main.ts
git commit -m "$(date --iso-8601=seconds)"
