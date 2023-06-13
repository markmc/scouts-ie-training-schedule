
all: next-training.csv

require_scouts_password:
ifndef SCOUTS_USERNAME
	$(error SCOUTS_USERNAME is not defined)
endif
ifndef SCOUTS_PASSWORD
	$(error SCOUTS_PASSWORD is not defined)
endif
ifndef SCOUTS_PROFILE_ID
	$(error SCOUTS_PROFILE_ID is not defined)
endif

next-training.json: require_scouts_password
	python get-next-training.py > next-training.json

next-training.csv: next-training.json
	echo "StartDate,CanBook,Location,Title" > next-training.csv
	cat next-training.json | jq -r '.[] | [.StartDate,.CanBook,.LocationTitle,.Title] | @csv' | tac >> next-training.csv

clean:
	rm -f next-training.json next-training.csv
