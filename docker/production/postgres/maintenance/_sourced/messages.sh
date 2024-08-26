#!/usr/bin/env bash

message_newline(){
  echo
}

message_debug(){
  # shellcheck disable=SC2145
  echo -e "DEBUG: ${@}"
}

message_welcome(){
  # shellcheck disable=SC2145
  echo -e "\e[1m${@}\e[0m"
}

message_warning(){
  # shellcheck disable=SC2145
  echo -e "\e[33mWARNING\e[0m: ${@}"
}

message_error(){
  # shellcheck disable=SC2145
  echo -e "\e[31mERROR\e[0m: ${@}"
}

message_info(){
  # shellcheck disable=SC2145
  echo -e "\e[37mINFO\e[0m: ${@}"
}

message_suggestion(){
  # shellcheck disable=SC2145
  echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

message_success(){
  # shellcheck disable=SC2145
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}