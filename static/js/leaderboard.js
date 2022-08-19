console.clear();

const team = [
{
  rank: 1,
  name: 'Zaid Mallik',
  handle: 'killam',
  img: 'https://therecord.media/wp-content/uploads/2021/09/hacker-hoodie.jpg',
  points: 136 },
{
  rank: 2,
  name: 'Avaneesh Kumar',
  handle: 'avaneeshh',
  img: 'https://therecord.media/wp-content/uploads/2021/09/hacker-hoodie.jpg',
  points: 131},
{
  rank: 3,
  name: 'Deepak Srinivas',
  handle: 'deepak',
  img: 'https://therecord.media/wp-content/uploads/2021/09/hacker-hoodie.jpg',
  points: 124},
{
  rank: 4,
  name: 'Akshaya',
  handle: 'akshayaa',
  img: 'https://therecord.media/wp-content/uploads/2021/09/hacker-hoodie.jpg',
  points: 114},];



const randomEmoji = () => {
  const emojis = ['👏', '👍', '🙌', '🤩', '🔥', '⭐️', '🏆', '💯'];
  let randomNumber = Math.floor(Math.random() * emojis.length);
  return emojis[randomNumber];
};

team.forEach(member => {
  let newRow = document.createElement('li');
  newRow.classList = 'c-list__item';
  newRow.innerHTML = `
		<div class="c-list__grid">
			<div class="c-flag c-place u-bg--transparent">${member.rank}</div>
			<div class="c-media">
				<img class="c-avatar c-media__img" src="${member.img}" />
				<div class="c-media__content">
					<div class="c-media__title">${member.name}</div>
					<a class="c-media__link u-text--small" href="https://127.0.0.1:8000/${member.handle}" target="_blank">@${member.handle}</a>
				</div>
			</div>
			<div class="u-text--right c-points">
				<div class="u-mt--8">
					<strong>${member.points}</strong> ${randomEmoji()}
				</div>
			</div>
		</div>
	`;
  if (member.rank === 1) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--yellow');
    newRow.querySelector('.c-points').classList.add('u-text--yellow');
  } else if (member.rank === 2) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--teal');
    newRow.querySelector('.c-points').classList.add('u-text--teal');
  } else if (member.rank === 3) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--orange');
    newRow.querySelector('.c-points').classList.add('u-text--orange');
  }
  list.appendChild(newRow);
});

// Find Winner by sorting points
let sortedPlayers = team.sort((a, b) => b.points - a.points);
let winner = sortedPlayers[0];

// Render winner card
const winnerCard = document.getElementById('winner');
winnerCard.innerHTML = `
	<div class="u-text-small u-text--medium u-mb--16">TOP PLAYER</div>
	<img class="c-avatar c-avatar--lg" src="${winner.img}"/>
	<h3 class="u-mt--16">${winner.name}</h3>
	<span class="u-text--teal u-text--small">${winner.handle}</span>
`;