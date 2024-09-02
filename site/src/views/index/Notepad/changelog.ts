import axios from 'axios';

export const getChangeLog = async() =>
{
  const changeLog = axios.get('https://api.github.com/repos/HydroRoll-Team/HydroRoll/releases/latest')
  .then(res => {
    console.log(res.data);
    const ChangeLogMessage ="## "+ res.data['tag_name']+"\n"+res.data['body'];
    return ChangeLogMessage;
  })
  .catch(err => {
    console.log(err);
    return err.toString();
  })
  return changeLog;
}
