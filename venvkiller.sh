#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'    

clear
echo -e "${CYAN}=============================================================================================${NC}"
echo -e "${CYAN}                               VENV KILLER v0.0.1                                            ${NC}"
echo -e "${CYAN}=============================================================================================${NC}"
echo  ""

mapfile -t venvs < <(find . -type d \( -name "venv" -o -name ".venv" -o -name "env" \) -exec test -d "{}/bin" -o -d "{}/Scripts" \; -print)
states=()
sizes=()

for i in ${!venvs[@]}; do
    states[$i]="AVAILABLE"
    sizes[$i]=$(du -sh "${venvs[$i]}" | cut -f1)
done

if [ ${#venvs[@]} -eq 0 ]; then
    echo -e "${RED}No virtual environments found.${NC}"
    exit 0
fi



while true; do
    clear
    echo -e "${CYAN}=============================================================================================${NC}"
    echo -e "${CYAN}                               VENV KILLER v0.0.1                                            ${NC}"
    echo -e "${CYAN}=============================================================================================${NC}"
    echo  ""
    echo -e "${YELLOW}INDEX |  STATUS   | SIZE |    PATH${NC}"
    echo -e "${BLUE}---------------------------------------------------------------------------------------------${NC}"
    for i in ${!venvs[@]}; do
        if [ ${states[$i]} == "AVAILABLE" ]; then
            echo -e "${YELLOW}[$i]${NC} - [${GREEN}${states[$i]}${NC}]: ${RED}${sizes[$i]}${NC} - ${venvs[$i]}"
        else
            echo -e "${YELLOW}[$i]${NC} - [ ${RED}${states[$i]}${NC} ]: ${GREEN}+${sizes[$i]}${NC} - ${venvs[$i]}"
        fi
    done

    echo -e "${BLUE}---------------------------------------------------------------------------------------------${NC}"
    echo ""

    read -p "Enter the number of the virtual environment to delete: " choice
    if [ "$choice" -ge 0 ] && [ "$choice" -lt ${#venvs[@]} ]; then
        rm -rf "${venvs[$choice]}"
        states[$choice]="DELETED"
       
    else
        echo -e "${RED}Invalid choice.${NC}"
    fi
done